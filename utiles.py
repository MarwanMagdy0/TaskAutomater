import json
import time

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