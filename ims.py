#!/usr/bin/env python3
import sys, re, requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar


# ─────────────── Worker Thread ─────────────── #
class Worker(QThread):
    finished = pyqtSignal(tuple)  # (main value, header text)

    def run(self):
        try:
            session    = requests.Session()
            login_url  = "http://45.82.67.20/ints/login"
            signin_url = "http://45.82.67.20/ints/signin"

            # 1) fetch login page
            resp  = session.get(login_url, timeout=10)
            soup  = BeautifulSoup(resp.text, "html.parser")
            divs  = soup.find_all("div", class_="col-sm-6")
            qtxt  = next((d.get_text(strip=True) for d in divs
                          if "What is" in d.get_text() and "=" in d.get_text()), None)
            if not qtxt:
                self.finished.emit(("CAPTCHA?", ""))
                return

            m = re.search(r'What is (.+?)=', qtxt)
            expr = m.group(1).strip() if m else None
            if not expr:
                self.finished.emit(("CAPTCHA Eval?", ""))
                return

            capt = eval(expr)

            # 2) submit credentials
            payload = {"username": "mohamedmagdy",
                       "password": "mohamedmagdy",
                       "capt":     str(capt)}
            headers = {"Referer": login_url,
                       "Origin":  "http://45.82.67.20",
                       "User-Agent": "Mozilla/5.0"}
            resp2 = session.post(signin_url, data=payload, headers=headers,
                                 allow_redirects=True, timeout=10)

            soup2 = BeautifulSoup(resp2.text, "html.parser")
            val_tag = soup2.find("h4", class_="fs-20 fw-bold mb-1 text-fixed-white")
            value   = val_tag.get_text(strip=True) if val_tag else "???"

            header_div = soup2.find("div", class_="main-header-center d-none d-lg-block")
            header_txt = header_div.get_text(strip=True) if header_div else ""

            self.finished.emit((value, header_txt))

        except Exception as e:
            print("Network error:", e)
            self.finished.emit(("Error", ""))


# ─────────────── Main UI ─────────────── #
class LoginFetcher(QWidget):
    REQUEST_INTERVAL_MS = 2000        # how often to hit the server
    ANIM_STEP_MS        = 20          # progress‑bar update speed

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Value Monitor")
        self.resize(500, 250)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        vbox = QVBoxLayout(self)

        # small header label
        self.header_lbl = QLabel("Header")
        self.header_lbl.setStyleSheet("font-size:12px;color:gray;")
        self.header_lbl.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        vbox.addWidget(self.header_lbl)

        # big value label
        self.value_lbl = QLabel("…")
        self.value_lbl.setAlignment(Qt.AlignCenter)
        self.value_lbl.setStyleSheet("font-size:64px;font-weight:700;color:#333;")
        vbox.addWidget(self.value_lbl)

        # progress bar
        self.progress  = QProgressBar()
        self.progress.setRange(0, 100)
        vbox.addWidget(self.progress)

        # timer driving the bar (stopped until a request finishes)
        self.anim = QTimer(self)
        self.anim.timeout.connect(self._tick_progress)
        self._p = 0

        # periodic request timer
        self.req_timer = QTimer(self)
        self.req_timer.timeout.connect(self._launch_worker)
        self.req_timer.start(self.REQUEST_INTERVAL_MS)

        # kick‑off first request immediately
        self._launch_worker()

    # ───────── helpers ───────── #
    def _tick_progress(self):
        self._p += 100 * self.ANIM_STEP_MS / self.REQUEST_INTERVAL_MS
        if self._p >= 100:
            self._p = 100
            self.anim.stop()          # countdown finished
        self.progress.setValue(int(self._p))

    def _reset_progress(self):
        self.anim.stop()
        self._p = 0
        self.progress.setValue(0)

    # ───────── network orchestration ───────── #
    def _launch_worker(self):
        # stop any ongoing animation → now we're busy
        self._reset_progress()

        # if previous worker still running, skip
        if hasattr(self, "_worker") and self._worker.isRunning():
            return

        self._worker = Worker()
        self._worker.finished.connect(self._update_ui)
        self._worker.start()

    def _update_ui(self, data):
        value, header = data
        self.value_lbl.setText(value)
        self.header_lbl.setText(header or "No header")

        # start animating until next request
        self._reset_progress()
        self.anim.start(self.ANIM_STEP_MS)


# ─────────────── run the app ─────────────── #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginFetcher()
    win.show()
    sys.exit(app.exec_())
