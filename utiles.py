from datetime import datetime, timedelta
from ims_client import IMSClient
import sqlite3
import time
import os
import phonenumbers

class EmailManager:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def insert_email_with_cookies(self, email: str, cookies: str):
        """Insert a new email with cookies into the emails table if it doesn't already exist."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.cursor.execute("SELECT id FROM emails WHERE email = ?", (email,))
        existing = self.cursor.fetchone()

        if existing:
            print(f"[!] Email already exists: {email}")
            return

        self.cursor.execute(
            "INSERT INTO emails (email, cookies, datetime) VALUES (?, ?, ?)",
            (email, cookies, now)
        )
        self.conn.commit()
        print(f"[+] Inserted email: {email}")

    def get_email_cookies_by_status(self):        
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
        
        self.cursor.execute(query)
        row = self.cursor.fetchone()
                
        return row["email_id"], row["email"], row["cookies"], row["log_count"], row["remaining_emails"] if row else (None, None, None, 0)
    
    def get_least_and_oldest_email(self):
        query = """
            SELECT 
                e.id AS email_id,
                e.email,
                e.cookies,
                COUNT(el.id) AS log_count
            FROM emails e
            LEFT JOIN email_logs el ON e.id = el.email_id
            GROUP BY e.id
            ORDER BY log_count ASC, e.datetime ASC
            LIMIT 1;
        """
        self.cursor.execute(query)
        row = self.cursor.fetchone()
                
        return row["email_id"], row["email"], row["cookies"], row["log_count"] if row else (None, None, None, 0)


    def log_status(self, email: str, status: str):
        """Log a new status for the given email address."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Step 1: Get the email ID
        self.cursor.execute("SELECT id FROM emails WHERE email = ?", (email,))
        result = self.cursor.fetchone()

        if result:
            email_id = result["id"]
            # Step 2: Log the status
            self.cursor.execute(
                "INSERT INTO email_logs (email_id, datetime, status) VALUES (?, ?, ?)",
                (email_id, now, status)
            )
            self.conn.commit()
        else:
            print(f"[!] Email not found: {email}")
            return
        
        time_logg(f"[+] {email} logged as : {status}")
    


class NumbersManager:
    def __init__(self, database_path):
        self.ims_client = IMSClient()
        self.conn = sqlite3.connect(database_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_available_number(self, country_code=""):
        """
        Return the oldest available number that is working and not archived,
        filtered by the given country_code prefix (empty string = no filter).
        Updates last_checked timestamp when a number is returned.
        """
        query = """
            SELECT id, number 
            FROM numbers 
            WHERE is_working = 1 AND is_archived = 0 
            AND number LIKE ? 
            ORDER BY 
                CASE 
                    WHEN last_checked IS NULL THEN 0 
                    ELSE 1 
                END,
                last_checked ASC
            LIMIT 1
        """

        self.cursor.execute(query, (f"{country_code}%",))
        row = self.cursor.fetchone()

        if row:
            number_id = row["id"]
            number = row["number"]
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            self.cursor.execute(
                "UPDATE numbers SET last_checked = ? WHERE id = ?",
                (now, number_id)
            )
            self.conn.commit()

            print(f"[+] Number {number} marked as last checked at {now}.")
            return number_id, number

        return None

    def update_number_status(self, number_id: int, is_working: bool):
        """Update the status and last_checked of a number. If working, increment hits."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if is_working:
            self.cursor.execute("""
                UPDATE numbers 
                SET is_working = ?, last_checked = ?, hits = hits + 1 
                WHERE id = ?
            """, (is_working, now, number_id))
        else:
            self.cursor.execute("""
                UPDATE numbers 
                SET is_working = ?, last_checked = ? 
                WHERE id = ?
            """, (is_working, now, number_id))

        self.conn.commit()
        time_logg(f"[+] Updated number ID {number_id} to {'[working]' if is_working else '[not working]'} at {now}.")

    def check_number(self, number_id, number, set_not_working = True):
        if self.ims_client.number_exists(number):
            self.update_number_status(number_id, is_working=True)
            return
        
        if set_not_working:
            self.update_number_status(number_id, is_working=False)
    
    @staticmethod
    def split_number(phone: str):
        try:
            parsed = phonenumbers.parse('+' + phone, None)

            country_code = parsed.country_code
            national_number = parsed.national_number

            return str(country_code), str(national_number)
        except phonenumbers.NumberParseException as e:
            return {"error": str(e)}
    
    def get_country_codes(self):
        self.cursor.execute("SELECT number FROM numbers")
        rows = self.cursor.fetchall()

        country_codes = set()

        for (num,) in rows:
            try:
                parsed = phonenumbers.parse('+' + num, None)
                country_codes.add(f"{parsed.country_code}")
            except phonenumbers.NumberParseException:
                continue  # skip invalid numbers

        return sorted(country_codes)

def time_logg(message: str):
    """Log a message with the current time."""
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{current_time}] {message}")

if __name__ == "__main__":
    email_id, email, cookies, log_count, total_logs = EmailManager.get_email_cookies_by_status()
    print(email_id, email, log_count, total_logs)
    EmailManager.log_status("3s3m0qb9tf", "CODE_SENT")