from datetime import datetime, timedelta
from ims_client import IMSClient
import sqlite3
import time
import os

conn = sqlite3.connect("database/bitly_database.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

class EmailManager:
    @staticmethod
    def insert_email_with_cookies(email: str, cookies: str):
        """Insert a new email with cookies into the emails table if it doesn't already exist."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute("SELECT id FROM emails WHERE email = ?", (email,))
        existing = cursor.fetchone()

        if existing:
            print(f"[!] Email already exists: {email}")
            return

        cursor.execute(
            "INSERT INTO emails (email, cookies, datetime) VALUES (?, ?, ?)",
            (email, cookies, now)
        )
        conn.commit()
        print(f"[+] Inserted email: {email}")

    @staticmethod
    def get_email_cookies_by_status():        
        query = """
            WITH log_summary AS (
                SELECT
                    e.id AS email_id,
                    e.email,
                    e.cookies,
                    COUNT(l.id) AS log_count,
                    MAX(l.datetime) AS last_log_time
                FROM emails e
                LEFT JOIN email_logs l
                    ON e.id = l.email_id AND l.datetime >= datetime('now', 'localtime', '-24 hours')
                GROUP BY e.id
            )
            SELECT email_id, email, cookies, log_count, last_log_time, COUNT(*) AS remaining_emails
            FROM log_summary
            WHERE
                log_count = 0
                OR (log_count IN (1, 2) AND (last_log_time IS NULL OR datetime(last_log_time) <= datetime('now', 'localtime', '-3 minutes')))
                OR (log_count = 3 AND (last_log_time IS NULL OR datetime(last_log_time) <= datetime('now', 'localtime', '-3 hours')))
                OR (log_count = 4 AND (last_log_time IS NULL OR datetime(last_log_time) <= datetime('now', 'localtime', '-4 hours')))
            LIMIT 1;
        """
        
        cursor.execute(query)
        row = cursor.fetchone()
                
        return row["email_id"], row["email"], row["cookies"], row["log_count"], row["remaining_emails"] if row else (None, None, None, 0)

    @staticmethod
    def log_status(email: str, status: str):
        """Log a new status for the given email address."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Step 1: Get the email ID
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM emails WHERE email = ?", (email,))
        result = cursor.fetchone()

        if result:
            email_id = result["id"]
            # Step 2: Log the status
            cursor.execute(
                "INSERT INTO email_logs (email_id, datetime, status) VALUES (?, ?, ?)",
                (email_id, now, status)
            )
            conn.commit()
        else:
            print(f"[!] Email not found: {email}")


class NumbersManager:
    def __init__(self):
        self.ims_client = IMSClient()

    def get_available_number(self):
        """Return the oldest available number that is working and not archived, and update its last_checked timestamp."""
        cursor.execute("""
            SELECT id, number 
            FROM numbers 
            WHERE is_working = 1 AND is_archived = 0 
            ORDER BY 
                CASE 
                    WHEN last_checked IS NULL THEN 0 
                    ELSE 1 
                END,
                last_checked ASC
            LIMIT 1
        """)
        row = cursor.fetchone()
        if row:
            number_id = row["id"]
            number = row["number"]
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            cursor.execute(
                "UPDATE numbers SET last_checked = ? WHERE id = ?",
                (now, number_id)
            )
            conn.commit()

            print(f"[+] Number {number} marked as last checked at {now}.")
            return number_id, number

        return None

    def update_number_status(self, number_id: int, is_working: bool):
        """Update the status and last_checked of a number. If working, increment hits."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if is_working:
            cursor.execute("""
                UPDATE numbers 
                SET is_working = ?, last_checked = ?, hits = hits + 1 
                WHERE id = ?
            """, (is_working, now, number_id))
        else:
            cursor.execute("""
                UPDATE numbers 
                SET is_working = ?, last_checked = ? 
                WHERE id = ?
            """, (is_working, now, number_id))

        conn.commit()
        time_logg(f"[+] Updated number ID {number_id} to {'[working]' if is_working else '[not working]'} at {now}.")

    def check_number(self, number_id, number):
        if self.ims_client.number_exists(number):
            self.update_number_status(number_id, is_working=True)
        else:
            self.update_number_status(number_id, is_working=False)

def time_logg(message: str):
    """Log a message with the current time."""
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{current_time}] {message}")

if __name__ == "__main__":
    email_id, email, cookies, log_count, total_logs = EmailManager.get_email_cookies_by_status()
    print(email_id, email, log_count, total_logs)
    EmailManager.log_status("3s3m0qb9tf", "CODE_SENT")