from datetime import datetime
import json
import time
import os
class PhoneStatusManager:
    def __init__(self, filename="numbers.json"):
        self.filename = filename
        self._load()

    def _load(self):
        with open(self.filename, "r") as f:
            self.data = json.load(f)

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=2)

    def get_next_number_status(self):
        self._load()
        min_number = None
        min_time = float("inf")

        for number, info in self.data.items():
            if info["is_working"] and info["last_checked"] < min_time:
                min_time = info["last_checked"]
                min_number = number

        if min_number is not None:
            # Update the last_checked time to the current time
            self.data[min_number]["last_checked"] = int(time.time())
            self._save()
            return min_number
        return None


    def update_number_status(self, number, is_working):
        if number not in self.data:
            raise ValueError(f"Number {number} not found in data.")

        self.data[number]["is_working"] = is_working
        self._save()
        print(f"Updated {number}: is_working={is_working}")


class EmailManager:
    def __init__(self, filepath='emails.json'):
        self.filepath = filepath
        self.load_data()

    def load_data(self):
        with open(self.filepath, 'r') as f:
            self.data = json.load(f)

    def save_data(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=2)

    def get_email(self):
        for email, info in self.data.items():
            if not info.get("used", False):
                self.data[email]["last_checked"] = int(time.time())
                self.save_data()
                return email
        return None  # No unused emails found

    def increment_email_usage(self, email):
        if email in self.data:
            self.data[email]["checks"] = self.data[email].get("checks", 0) + 1
            self.save_data()
        else:
            raise ValueError(f"Email {email} not found in data.")

    def restore_email(self, email):
        if email in self.data:
            self.data[email]["used"] = False
            self.save_data()
        else:
            raise ValueError(f"Email {email} not found in data.")
    
    def email_is_used(self, email):
        if email in self.data:
            self.data[email]["used"] = True
            self.save_data()
        else:
            raise ValueError(f"Email {email} not found in data.")


class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    self.data = json.load(f)
            except json.JSONDecodeError:
                self.data = {}
        else:
            self._save()

    def _save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=2)

    def _current_time_am_pm(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %I:%M:%S %p")

    def log_trigger(self, key):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(self._current_time_am_pm())
        self._save()

    def get_logs(self, key):
        return self.data.get(key, [])

    def all_data(self):
        return self.data



def time_logg(message: str):
    """Log a message with the current time."""
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{current_time}] {message}")

if __name__ == "__main__":
    manager = PhoneStatusManager("numbers.json")
    # Get the number with the earliest last_checked time
    number = manager.get_next_number_status()
    print(f"Next number: {number}")

    # Update a number's status
    manager.update_number_status(number, is_working=False)