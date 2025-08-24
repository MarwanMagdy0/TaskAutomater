import sys, re, requests, os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QUrl, QPoint, QSize
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar,
    QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QPushButton, QStackedLayout, QFrame
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ────────────────────── Config ──────────────────────
BASE_URL = "http://45.82.67.20"
LOGIN_URL = f"{BASE_URL}/ints/login"
SIGNIN_URL = f"{BASE_URL}/ints/signin"
DASHBOARD_URL = f"{BASE_URL}/ints/client/SMSDashboard"
CDR_URL = f"{BASE_URL}/ints/client/res/data_smscdr.php"

USERNAME = "MohamedMagdy1"
PASSWORD = "MohamedMagdy1"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

# ────────────────────── Helpers ──────────────────────
def _solve_captcha(text: str) -> int:
    m = re.search(r'What\s+is\s+(\d+)\s*([\+\-\*/])\s*(\d+)', text or "", flags=re.I)
    if not m: raise ValueError("Captcha not found")
    a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
    return a+b if op=="+" else a-b if op=="-" else a*b if op=="*" else (a//b if b!=0 else 0)

def _find_etkk(soup: BeautifulSoup) -> str:
    etkk_input = soup.find("input", {"name": "etkk"})
    return etkk_input["value"].strip() if etkk_input and etkk_input.has_attr("value") else ""

# ────────────────────── Worker Thread ────────────────────── 
class Worker(QThread):
    finished = pyqtSignal(tuple)      # (main value, header text)
    new_sms_data = pyqtSignal(list)   # [[timestamp, range, number], ...]

    def run(self):
        try:
            session = requests.Session()
            session.headers.update({"User-Agent": UA})

            if self.isInterruptionRequested(): return
            r_login = session.get(LOGIN_URL, timeout=15); r_login.raise_for_status()
            soup_login = BeautifulSoup(r_login.text, "html.parser")

            qtxt = None
            for d in soup_login.select("div.col-sm-6"):
                t = d.get_text(" ", strip=True)
                if "What is" in t and "=" in t: qtxt = t; break
            if not qtxt: raise RuntimeError("Could not locate math captcha on login page.")
            capt_value = _solve_captcha(qtxt)
            etkk_value = _find_etkk(soup_login)

            if self.isInterruptionRequested(): return
            payload = {"username": USERNAME, "password": PASSWORD, "capt": str(capt_value)}
            if etkk_value: payload["etkk"] = etkk_value
            headers = {"User-Agent": UA, "Referer": LOGIN_URL, "Origin": BASE_URL}
            r_signin = session.post(SIGNIN_URL, data=payload, headers=headers, allow_redirects=True, timeout=20); r_signin.raise_for_status()

            if self.isInterruptionRequested(): return
            r_dash = session.get(DASHBOARD_URL, headers={"User-Agent": UA}, timeout=20); r_dash.raise_for_status()
            soup_dash = BeautifulSoup(r_dash.text, "html.parser")
            val_tag = soup_dash.select_one("h4.fs-20.fw-bold.mb-1.text-fixed-white")
            value = val_tag.get_text(strip=True) if val_tag else "???"
            header_div = soup_dash.select_one("div.main-header-center.d-none.d-lg-block")
            header_txt = header_div.get_text(" ", strip=True) if header_div else ""
            self.finished.emit((value, header_txt))

            if self.isInterruptionRequested(): return
            from_time = datetime.now() - timedelta(hours=3, minutes=10)
            to_time = datetime.now()
            cdr_params = {
                "fdate1": from_time.strftime("%Y-%m-%d %H:%M:%S"),
                "fdate2": to_time.strftime("%Y-%m-%d %H:%M:%S"),
                "iDisplayLength": "15",
            }
            ajax_headers = {
                "User-Agent": UA,
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": f"{BASE_URL}/ints/client/SMSCDRStats",
            }
            r_cdr = session.get(CDR_URL, params=cdr_params, headers=ajax_headers, timeout=20); r_cdr.raise_for_status()
            data = r_cdr.json(); aa = data.get("aaData", []) or []

            formatted = []
            for row in aa:
                try:
                    dt = datetime.strptime(str(row[0]), "%Y-%m-%d %H:%M:%S") + timedelta(hours=3)
                    time_str = dt.strftime("%I:%M:%S %p")
                    formatted.append([time_str, str(row[1]), str(row[2])])
                except Exception:
                    continue
            self.new_sms_data.emit(list(reversed(formatted))[:50])

        except Exception as e:
            self.finished.emit((f"Error", f"{type(e).__name__}: {e}"))

# ──────────────────── Floating UI (click to open, drag to move) ────────────────────
class LoginFetcher(QWidget):
    # Poll every 5s, and the progress bar fills exactly over those 5s
    REQUEST_INTERVAL_MS = 5000
    ANIM_STEP_MS = 20

    COLLAPSED_SIZE = QSize(100, 100)
    EXPANDED_SIZE = QSize(520, 640)

    DRAG_THRESHOLD = 6  # pixels to distinguish drag from click

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self._is_collapsed = True
        self._press_pos_global = None
        self._press_win_pos = None
        self._dragging = False

        # Card
        self.card = QFrame(self); self.card.setObjectName("card")
        self.card.setStyleSheet("#card { background:#ffffff; border-radius:14px; }")
        shadow = QGraphicsDropShadowEffect(self); shadow.setBlurRadius(24); shadow.setOffset(0, 8)
        self.card.setGraphicsEffect(shadow)

        self.stack = QStackedLayout(self.card)

        # ===== Collapsed “icon” =====
        self.value_only = QWidget()
        v_c = QVBoxLayout(self.value_only); v_c.setContentsMargins(12,12,12,12); v_c.setSpacing(6)

        self.value_lbl_big = QLabel("…")
        self.value_lbl_big.setAlignment(Qt.AlignCenter)
        self.value_lbl_big.setStyleSheet("font-size:20px;font-weight:700;color:#3366cc;")  # smaller label
        v_c.addStretch(1)
        v_c.addWidget(self.value_lbl_big, 0, Qt.AlignCenter)

        # Thin modern progress bar (collapsed)
        self.progress_small = QProgressBar()
        self.progress_small.setRange(0, 100)
        self.progress_small.setTextVisible(False)
        self.progress_small.setFixedHeight(4)
        self.progress_small.setStyleSheet("""
            QProgressBar {
                background-color: #eef3ff;
                border: none;
                border-radius: 2px;
            }
            QProgressBar::chunk {
                border-radius: 2px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #7aa6ff, stop:1 #3366cc);
            }
        """)
        v_c.addWidget(self.progress_small)
        v_c.addStretch(1)

        self.stack.addWidget(self.value_only)

        # ===== Expanded view =====
        self.expanded = QWidget(); vbox = QVBoxLayout(self.expanded)
        vbox.setContentsMargins(12,12,12,12); vbox.setSpacing(8)

        titlebar = QHBoxLayout(); titlebar.setSpacing(6)
        self.title_lbl = QLabel("Live Value Monitor")
        self.title_lbl.setStyleSheet("font-size:12px;color:#444;font-weight:600;")
        titlebar.addWidget(self.title_lbl); titlebar.addStretch(1)

        self.btn_collapse = QPushButton("–"); self.btn_close = QPushButton("×")
        for b in (self.btn_collapse, self.btn_close):
            b.setFixedSize(28,24)
            b.setStyleSheet("""
                QPushButton { border:none; border-radius:6px; background:#f1f1f1; font-size:16px; }
                QPushButton:hover { background:#e5e5e5; } QPushButton:pressed { background:#dcdcdc; }
            """)
        titlebar.addWidget(self.btn_collapse); titlebar.addWidget(self.btn_close)
        vbox.addLayout(titlebar)

        self.header_lbl = QLabel("Header")
        self.header_lbl.setStyleSheet("font-size:11px;color:gray;")
        self.header_lbl.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        vbox.addWidget(self.header_lbl)

        self.value_lbl = QLabel("…")
        self.value_lbl.setAlignment(Qt.AlignCenter)
        self.value_lbl.setStyleSheet("font-size:28px;font-weight:700;color:#3366cc;")  # smaller label
        vbox.addWidget(self.value_lbl)

        # Thin modern progress bar (expanded)
        self.progress = QProgressBar(); self.progress.setRange(0,100)
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(6)
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: #eef3ff;
                border: none;
                border-radius: 3px;
            }
            QProgressBar::chunk {
                border-radius: 3px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #7aa6ff, stop:1 #3366cc);
            }
        """)
        vbox.addWidget(self.progress)

        # Table
        self.table = QTableWidget(); self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Timestamp", "Range", "Number"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers); self.table.verticalHeader().setVisible(False)
        self.table.setStyleSheet("""
            QTableWidget { font-family:'Segoe UI'; font-size:13px; border:1px solid #ddd; gridline-color:#ccc;
                           background:#fafafa; alternate-background-color:#f0f0f0; }
            QHeaderView::section { background:#e0e0e0; font-weight:bold; padding:6px; border:1px solid #ddd; }
            QTableWidget::item { padding:6px; border:none; }
        """)
        self.table.setAlternatingRowColors(True)
        header = self.table.horizontalHeader(); header.setSectionResizeMode(QHeaderView.Stretch)
        vbox.addWidget(self.table)

        self.stack.addWidget(self.expanded)

        # timers + media
        self.anim = QTimer(self); self.anim.timeout.connect(self._tick_progress); self._p = 0
        self.req_timer = QTimer(self); self.req_timer.timeout.connect(self._launch_worker)
        self.req_timer.start(self.REQUEST_INTERVAL_MS)

        self._last_value_text = None
        self._worker = None

        self._player = QMediaPlayer()
        mp3_path = os.path.abspath("assets/money_sound.mp3")
        if os.path.exists(mp3_path):
            self._player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_path)))

        self.btn_collapse.clicked.connect(self.collapse)
        self.btn_close.clicked.connect(self._handle_close)

        # initial state: collapsed icon
        self.setFixedSize(self.COLLAPSED_SIZE)
        self._apply_card_geometry()
        self.stack.setCurrentIndex(0)

        self._launch_worker()

    # geometry
    def _apply_card_geometry(self):
        self.card.setGeometry(0, 0, self.width(), self.height())

    # state (instant)
    def expand(self):
        if self._is_collapsed:
            self._is_collapsed = False
            self.stack.setCurrentIndex(1)
            self.setFixedSize(self.EXPANDED_SIZE)
            self._apply_card_geometry()

    def collapse(self):
        if not self._is_collapsed:
            self._is_collapsed = True
            self.stack.setCurrentIndex(0)
            self.setFixedSize(self.COLLAPSED_SIZE)
            self._apply_card_geometry()

    # progress (fills over REQUEST_INTERVAL_MS = 5000 ms)
    def _tick_progress(self):
        self._p += 100 * self.ANIM_STEP_MS / self.REQUEST_INTERVAL_MS
        if self._p >= 100:
            self._p = 100
            self.anim.stop()
        # update both bars (collapsed + expanded)
        self.progress_small.setValue(int(self._p))
        self.progress.setValue(int(self._p))

    def _reset_progress(self):
        self.anim.stop()
        self._p = 0
        self.progress_small.setValue(0)
        self.progress.setValue(0)

    # worker lifecycle
    def _launch_worker(self):
        self._reset_progress()
        if self._worker is not None and self._worker.isRunning(): return
        self._worker = Worker()
        self._worker.finished.connect(self._update_ui)
        self._worker.new_sms_data.connect(self._update_table)
        self._worker.start()
        # start ticking immediately for a fresh 5s cycle
        self.anim.start(self.ANIM_STEP_MS)

    def _stop_worker(self):
        if self._worker is None: return
        if self._worker.isRunning():
            self._worker.requestInterruption()
            self._worker.wait(2000)
            if self._worker.isRunning():
                self._worker.terminate()
                self._worker.wait()
        self._worker = None

    def _update_ui(self, data):
        value, header = data
        try:
            if self._last_value_text != value and value not in ("Error", "???"):
                self._player.setPosition(0); self._player.play()
                self._last_value_text = value
        except Exception:
            pass

        self.value_lbl_big.setText(value)
        self.value_lbl.setText(value)
        if not self._is_collapsed:
            self.header_lbl.setText(header or "No header")
        # (progress keeps running regardless of view)

    def _update_table(self, sms_list):
        if self._is_collapsed: return
        self.table.setRowCount(0)
        for i, row in enumerate(sms_list):
            self.table.insertRow(i)
            for j, item in enumerate(row):
                qitem = QTableWidgetItem(item); qitem.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(i, j, qitem)

    # ---- click vs drag behavior (NO open on drag) ----
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self._press_pos_global = e.globalPos()
            self._press_win_pos = self.pos()
            self._dragging = False
        super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self._press_pos_global is not None and (e.buttons() & Qt.LeftButton):
            delta = e.globalPos() - self._press_pos_global
            if (abs(delta.x()) > self.DRAG_THRESHOLD) or (abs(delta.y()) > self.DRAG_THRESHOLD):
                self._dragging = True
                self.move(self._press_win_pos + delta)
        super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            if not self._dragging:
                if self._is_collapsed:
                    self.expand()
        self._press_pos_global = None
        self._press_win_pos = None
        self._dragging = False
        super().mouseReleaseEvent(e)

    # close handling (ensure no background process)
    def _handle_close(self):
        self.close()

    def closeEvent(self, event):
        try:
            self.req_timer.stop()
            self.anim.stop()
        except Exception:
            pass
        self._stop_worker()
        QApplication.instance().quit()
        event.accept()

# ─────────────────── Run the App ───────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginFetcher()
    screen = app.primaryScreen().availableGeometry()
    win.move(screen.center() - win.rect().center())
    win.show()
    sys.exit(app.exec_())
