import sys
import sqlite3
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QTextEdit, QDialogButtonBox, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

DB_PATH = "database/database.db"

class AddNumbersDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Numbers")
        self.resize(400, 300)

        layout = QVBoxLayout(self)
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Paste numbers here...")
        layout.addWidget(self.text_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_numbers(self):
        text = self.text_edit.toPlainText()
        return list(set(re.findall(r'\b\d{4,}\b', text)))  # unique numbers


class NumberTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Tracker")
        self.resize(700, 550)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title
        title = QLabel("📱 Number Tracker")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title)

        # Top Controls (Add/Delete + Stats)
        top_controls_layout = QHBoxLayout()

        self.add_button = QPushButton("➕ Add Numbers")
        self.delete_all_button = QPushButton("🗑️ Delete All (Not Archived)")
        for btn in [self.add_button, self.delete_all_button]:
            btn.setStyleSheet("font-size: 13px; padding: 6px 12px;")
        top_controls_layout.addWidget(self.add_button)
        top_controls_layout.addWidget(self.delete_all_button)

        top_controls_layout.addStretch()

        self.top_stats_label = QLabel("Working: 0 | Not Working: 0")
        self.top_stats_label.setStyleSheet("font-size: 14px; padding: 4px;")
        top_controls_layout.addWidget(self.top_stats_label)

        self.layout.addLayout(top_controls_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Number", "Last Checked", "Status", "Hits"])
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().setVisible(False)
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
                padding: 4px;
            }
        """)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Bottom Controls (Archive Buttons + Total Info)
        bottom_layout = QHBoxLayout()

        self.archive_all_button = QPushButton("📦 Archive All")
        self.archive_not_working_button = QPushButton("❌ Archive Not Working")
        for btn in [self.archive_all_button, self.archive_not_working_button]:
            btn.setStyleSheet("font-size: 13px; padding: 6px 12px;")
            bottom_layout.addWidget(btn)

        bottom_layout.addStretch()

        self.bottom_stats_label = QLabel("Total: 0 | Total Hits: 0")
        self.bottom_stats_label.setStyleSheet("font-size: 13px; color: #444; padding-left: 10px;")
        bottom_layout.addWidget(self.bottom_stats_label)

        self.layout.addLayout(bottom_layout)

        # Connect
        self.archive_all_button.clicked.connect(self.archive_all)
        self.archive_not_working_button.clicked.connect(self.archive_not_working)
        self.delete_all_button.clicked.connect(self.delete_all_not_archived)
        self.add_button.clicked.connect(self.show_add_dialog)

        # Auto refresh
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.load_data)
        self.refresh_timer.start(10000)  # 10 seconds

        self.load_data()

    def get_connection(self):
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def load_data(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT number, last_checked, is_working, hits
            FROM numbers
            WHERE is_archived = 0
            ORDER BY last_checked DESC
        """)
        rows = cur.fetchall()
        conn.close()

        self.table.setSortingEnabled(False)
        self.table.setRowCount(len(rows))
        working = not_working = total_hits = 0

        for row_idx, (number, last_checked, is_working, hits) in enumerate(rows):
            self._set_table_item(row_idx, 0, number)
            self._set_table_item(row_idx, 1, str(last_checked or ""))
            status = "✅ Working" if is_working else "❌ Not Working"
            self._set_table_item(row_idx, 2, status)
            self._set_table_item(row_idx, 3, str(hits or 0))

            working += int(is_working)
            not_working += int(not is_working)
            total_hits += hits or 0

        self.top_stats_label.setText(f"✅ Working: {working} | ❌ Not Working: {not_working}")
        self.bottom_stats_label.setText(f"📊 Total: {len(rows)} | 🔁 Total Hits: {total_hits}")
        self.table.setSortingEnabled(True)

    def _set_table_item(self, row, col, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row, col, item)

    def archive_all(self):
        if self.ask("Are you sure you want to archive all numbers?"):
            conn = self.get_connection()
            conn.execute("UPDATE numbers SET is_archived = 1 WHERE is_archived = 0")
            conn.commit()
            conn.close()
            self.load_data()

    def archive_not_working(self):
        if self.ask("Are you sure you want to archive all not-working numbers?"):
            conn = self.get_connection()
            conn.execute("UPDATE numbers SET is_archived = 1 WHERE is_archived = 0 AND is_working = 0")
            conn.commit()
            conn.close()
            self.load_data()

    def delete_all_not_archived(self):
        if self.ask("Are you sure you want to DELETE all unarchived numbers? This cannot be undone."):
            conn = self.get_connection()
            conn.execute("DELETE FROM numbers WHERE is_archived = 0")
            conn.commit()
            conn.close()
            self.load_data()

    def show_add_dialog(self):
        dialog = AddNumbersDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            new_numbers = dialog.get_numbers()
            if new_numbers:
                conn = self.get_connection()
                cur = conn.cursor()
                added = 0
                for num in new_numbers:
                    cur.execute("SELECT id FROM numbers WHERE number = ?", (num,))
                    if not cur.fetchone():
                        cur.execute("INSERT INTO numbers (number, last_checked, is_working, hits) VALUES (?, 0, 1, 0)", (num,))
                        added += 1
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Success", f"{added} new number(s) added.")
                self.load_data()

    def ask(self, question):
        return QMessageBox.question(self, "Confirm", question, QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NumberTrackerApp()
    win.show()
    sys.exit(app.exec_())
