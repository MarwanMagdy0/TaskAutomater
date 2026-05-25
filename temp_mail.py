import requests
import time
from faker import Faker


class MailTM:
    BASE_URL = "https://api.mail.tm"

    def __init__(self, password="temp", locale="en_US"):
        self.session = requests.Session()
        self.fake = Faker(locale)
        self.password = password
        self.email = None
        self.token = None
        self.seen = set()

    def make_email_name(self):
        first = self.fake.first_name().lower()
        last = self.fake.last_name().lower()
        number = int(time.time())

        return f"{first}{last}{number}"

    def get_domain(self):
        res = self.session.get(f"{self.BASE_URL}/domains")
        res.raise_for_status()

        domains = res.json().get("hydra:member", [])

        if not domains:
            raise Exception("No mail.tm domains available")

        return domains[0]["domain"]

    def create_account(self):
        domain = self.get_domain()
        email_name = self.make_email_name()
        self.email = f"{email_name}@{domain}"

        print("Email:", self.email)

        res = self.session.post(
            f"{self.BASE_URL}/accounts",
            json={
                "address": self.email,
                "password": self.password,
            },
        )

        if res.status_code not in (200, 201):
            raise Exception(f"Account error: {res.text}")

        self.login()
        return self.email

    def login(self):
        if not self.email:
            raise Exception("No email created yet")

        res = self.session.post(
            f"{self.BASE_URL}/token",
            json={
                "address": self.email,
                "password": self.password,
            },
        )

        res.raise_for_status()

        self.token = res.json()["token"]

        self.session.headers.update({
            "Authorization": f"Bearer {self.token}"
        })

        return self.token

    def get_messages(self):
        res = self.session.get(f"{self.BASE_URL}/messages")
        res.raise_for_status()

        return res.json().get("hydra:member", [])

    def get_message(self, message_id):
        res = self.session.get(f"{self.BASE_URL}/messages/{message_id}")
        res.raise_for_status()

        return res.json()

    def wait_for_new_message(self, timeout=120, interval=5):
        print("Waiting for messages...\n")

        start = time.time()

        while time.time() - start < timeout:
            inbox = self.get_messages()

            for msg in inbox:
                if msg["id"] in self.seen:
                    continue

                self.seen.add(msg["id"])

                return self.get_message(msg["id"])

            time.sleep(interval)

        raise TimeoutError("No new message received")

    def print_message(self, message):
        print("📩 NEW MESSAGE")
        print("From:", message.get("from", {}).get("address"))
        print("Subject:", message.get("subject"))
        print("Text:", message.get("text"))
        print("-" * 40)

if __name__ == "__main__":
    mail = MailTM()

    email = mail.create_account()

    message = mail.wait_for_new_message(timeout=120, interval=5)

    mail.print_message(message)