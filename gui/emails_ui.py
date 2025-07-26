import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QTableWidget, QTableWidgetItem,
    QHeaderView, QLabel, QCheckBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from datetime import datetime, timedelta

DB_PATH = "database/database.db"

def get_total_logs_from_3am():
    now = datetime.now()
    today_3am = now.replace(hour=3, minute=0, second=0, microsecond=0)
    if now < today_3am:
        today_3am -= timedelta(days=1)
    start_time = today_3am.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM email_logs WHERE datetime >= ?", (start_time,))
    count = cur.fetchone()[0]
    conn.close()
    return count

class FilteredEmailLogsViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Activity Overview (Last 24h)")
        self.resize(400, 600)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(12, 10, 12, 10)
        main_layout.setSpacing(10)

        # Header
        self.title_label = QLabel("Email Activity Overview (Last 24h)")
        self.title_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # Controls layout
        top_controls = QHBoxLayout()
        top_controls.setSpacing(15)

        top_controls.addWidget(QLabel("Date:"))
        self.date_combo = QComboBox()
        self.date_combo.setMinimumWidth(160)
        self.date_combo.setStyleSheet("""
            QComboBox {
                padding: 5px;
                font-size: 13px;
            }
        """)
        self.date_combo.currentIndexChanged.connect(self.update_table)
        top_controls.addWidget(self.date_combo)

        self.summary_checkbox = QCheckBox("Summary Mode")
        self.summary_checkbox.setStyleSheet("font-size: 13px;")
        self.summary_checkbox.stateChanged.connect(self.update_table)
        top_controls.addWidget(self.summary_checkbox)

        self.total_logs_label = QLabel("Total Logs Since 3 AM: ...")
        self.total_logs_label.setStyleSheet("font-size: 13px; color: #444; padding-left: 10px;")
        top_controls.addStretch()
        top_controls.addWidget(self.total_logs_label)

        main_layout.addLayout(top_controls)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Email", "Date Time", "Status"])
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.table.setStyleSheet("""
            QTableWidget {
                font-size: 13px;
                alternate-background-color: #f9f9f9;
                background-color: #ffffff;
                gridline-color: #e0e0e0;
            }
            QHeaderView::section {
                background-color: #eeeeee;
                font-weight: bold;
                padding: 6px;
                border: none;
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        main_layout.addWidget(self.table)

        # Bottom stats label
        self.stats_label = QLabel("Stats: ...")
        self.stats_label.setAlignment(Qt.AlignLeft)
        self.stats_label.setStyleSheet("padding: 5px; color: #444; font-size: 13px;")
        main_layout.addWidget(self.stats_label)

        self.setLayout(main_layout)

        self.load_dates()
        self.update_table()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_table)
        self.timer.start(10000)

    def get_connection(self):
        return sqlite3.connect(DB_PATH)

    def load_dates(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT DATE(datetime) FROM emails ORDER BY datetime DESC")
        dates = [row[0] for row in cur.fetchall()]
        self.date_combo.clear()
        self.date_combo.addItems(dates)
        conn.close()

    def update_table(self):
        if self.date_combo.count() == 0:
            return

        selected_date = self.date_combo.currentText()
        now = datetime.now()
        since_24h = now - timedelta(hours=24)
        since_24h_str = since_24h.strftime("%Y-%m-%d %H:%M:%S")

        conn = self.get_connection()
        cur = conn.cursor()

        if self.summary_checkbox.isChecked():
            cur.execute("""
                SELECT emails.email, 
                       COUNT(email_logs.id) AS log_count
                FROM emails
                LEFT JOIN email_logs 
                    ON emails.id = email_logs.email_id 
                    AND email_logs.datetime >= ?
                WHERE DATE(emails.datetime) = ?
                GROUP BY emails.id
                ORDER BY log_count DESC
            """, (since_24h_str, selected_date))
            rows = cur.fetchall()

            self.table.setSortingEnabled(False)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(["Email", "Log Count"])
            self.table.setRowCount(len(rows))
            for row_idx, (email, count) in enumerate(rows):
                self._set_table_item(row_idx, 0, email)
                self._set_table_item(row_idx, 1, str(count))
            self.table.setSortingEnabled(True)

            self.stats_label.setText(f"📊 Logs: {sum(c for _, c in rows)} | Emails: {len(rows)}")

        else:
            cur.execute("""
                SELECT emails.email, email_logs.datetime, email_logs.status
                FROM email_logs
                JOIN emails ON email_logs.email_id = emails.id
                WHERE DATE(emails.datetime) = ?
                  AND email_logs.datetime >= ?
                ORDER BY email_logs.datetime DESC
            """, (selected_date, since_24h_str))
            rows = cur.fetchall()

            self.table.setSortingEnabled(False)
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["Email", "Date Time", "Status"])
            self.table.setRowCount(len(rows))
            for row_idx, (email, dt, status) in enumerate(rows):
                self._set_table_item(row_idx, 0, email)
                self._set_table_item(row_idx, 1, dt)
                self._set_table_item(row_idx, 2, status)
            self.table.setSortingEnabled(True)

            self.stats_label.setText(f"📊 Total Logs: {len(rows)}")

        total_logs_3am = get_total_logs_from_3am()
        self.total_logs_label.setText(f"🕒 Total Logs Since 3 AM: {total_logs_3am}")

        conn.close()

    def _set_table_item(self, row, col, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = FilteredEmailLogsViewer()
    viewer.show()
    sys.exit(app.exec_())
