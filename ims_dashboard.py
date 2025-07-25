#!/usr/bin/env python3
import sys, re, requests, os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QUrl
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ────────────────────── Worker Thread ────────────────────── 
class Worker(QThread):
    finished = pyqtSignal(tuple)      # (main value, header text)
    new_sms_data = pyqtSignal(list)   # [[timestamp, range, number], ...]

    def run(self):
        try:
            session = requests.Session()
            base_url = "http://45.82.67.20"
            login_url = f"{base_url}/ints/login"
            signin_url = f"{base_url}/ints/signin"
            data_url = f"{base_url}/ints/client/res/data_smscdr.php"

            # Step 1: CAPTCHA
            resp = session.get(login_url, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            divs = soup.find_all("div", class_="col-sm-6")
            qtxt = next((d.get_text(strip=True) for d in divs if "What is" in d.text and "=" in d.text), None)
            capt = eval(re.search(r'What is (.+?)=', qtxt).group(1).strip()) if qtxt else None

            # Step 2: Login
            payload = {"username": "22momagdy", "password": "22momagdy22", "capt": str(capt)}
            headers = {"Referer": login_url, "Origin": base_url, "User-Agent": "Mozilla/5.0"}
            resp2 = session.post(signin_url, data=payload, headers=headers, allow_redirects=True, timeout=10)

            # Step 3: Dashboard value
            soup2 = BeautifulSoup(resp2.text, "html.parser")
            val_tag = soup2.find("h4", class_="fs-20 fw-bold mb-1 text-fixed-white")
            value = val_tag.get_text(strip=True) if val_tag else "???"

            header_div = soup2.find("div", class_="main-header-center d-none d-lg-block")
            header_txt = header_div.get_text(strip=True) if header_div else ""

            self.finished.emit((value, header_txt))

            # Step 4: SMSCDR fetch
            from_time = datetime.now() - timedelta(hours=3, minutes=10)
            to_time = datetime.now()

            smscdr_params = {
                "fdate1": from_time.strftime("%Y-%m-%d %H:%M:%S"),
                "fdate2": to_time.strftime("%Y-%m-%d %H:%M:%S"),
                "iDisplayLength": "15",
            }

            ajax_headers = {
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": f"{base_url}/ints/client/SMSCDRStats"
            }

            resp3 = session.get(data_url, params=smscdr_params, headers=ajax_headers, timeout=10)
            sms_data = resp3.json().get("aaData", [])

            formatted = []
            for row in sms_data:
                try:
                    dt = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") + timedelta(hours=3)
                    time_str = dt.strftime("%Y-%m-%d %I:%M:%S %p")
                    formatted.append([time_str, row[1], row[2]])
                except Exception:
                    continue

            self.new_sms_data.emit(list(reversed(formatted))[:50])

        except Exception:
            self.finished.emit(("Error", ""))


# ──────────────────── Main UI ──────────────────── 
class LoginFetcher(QWidget):
    REQUEST_INTERVAL_MS = 10000
    ANIM_STEP_MS = 20

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Value Monitor")
        self.resize(700, 500)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        vbox = QVBoxLayout(self)

        self.header_lbl = QLabel("Header")
        self.header_lbl.setStyleSheet("font-size:12px;color:gray;")
        self.header_lbl.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        vbox.addWidget(self.header_lbl)

        self.value_lbl = QLabel("…")
        self.value_lbl.setAlignment(Qt.AlignCenter)
        self.value_lbl.setStyleSheet("font-size:64px;font-weight:700;color:#333;")
        vbox.addWidget(self.value_lbl)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        vbox.addWidget(self.progress)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Timestamp", "Range", "Number"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setStyleSheet("font-family: Consolas; font-size: 13px;")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        vbox.addWidget(self.table)

        self.anim = QTimer(self)
        self.anim.timeout.connect(self._tick_progress)
        self._p = 0

        self.req_timer = QTimer(self)
        self.req_timer.timeout.connect(self._launch_worker)
        self.req_timer.start(self.REQUEST_INTERVAL_MS)

        self._last_value_text = None

        self._player = QMediaPlayer()
        mp3_path = os.path.abspath("assets/money_sound.mp3")
        print("Loading MP3 from:", mp3_path)
        if os.path.exists(mp3_path):
            self._player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_path)))
        else:
            print("MP3 file not found!")

        self._player.mediaStatusChanged.connect(lambda s: print("Media status:", s))
        self._player.error.connect(lambda e: print("Media error:", self._player.errorString()))

        self._launch_worker()

    def _tick_progress(self):
        self._p += 100 * self.ANIM_STEP_MS / self.REQUEST_INTERVAL_MS
        if self._p >= 100:
            self._p = 100
            self.anim.stop()
        self.progress.setValue(int(self._p))

    def _reset_progress(self):
        self.anim.stop()
        self._p = 0
        self.progress.setValue(0)

    def _launch_worker(self):
        self._reset_progress()
        if hasattr(self, "_worker") and self._worker.isRunning():
            return

        self._worker = Worker()
        self._worker.finished.connect(self._update_ui)
        self._worker.new_sms_data.connect(self._update_table)
        self._worker.start()

    def _update_ui(self, data):
        value, header = data

        # Sound only if value_lbl text changed
        if self._last_value_text != value:
            print(f"Value changed: {self._last_value_text} -> {value}")
            self._player.setPosition(0)
            self._player.play()
            self._last_value_text = value

        self.value_lbl.setText(value)
        self.header_lbl.setText(header or "No header")
        self._reset_progress()
        self.anim.start(self.ANIM_STEP_MS)

    def _update_table(self, sms_list):
        self.table.setRowCount(0)

        for i, row in enumerate(sms_list):
            self.table.insertRow(i)
            for j, item in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(item))


# ─────────────────── Run the App ───────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginFetcher()
    win.show()
    sys.exit(app.exec_())
