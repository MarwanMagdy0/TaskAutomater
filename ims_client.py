import re
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


class IMSClient:
    BASE_URL = "http://45.82.67.20"

    def __init__(self, username="22momagdy", password="22momagdy22"):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        })
        self.username = username
        self.password = password
        self.logged_in = False

    def _solve_captcha(self, html):
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.find_all("div", class_="col-sm-6")
        qtxt = next((d.get_text(strip=True) for d in divs if "What is" in d.text and "=" in d.text), None)
        return eval(re.search(r'What is (.+?)=', qtxt).group(1).strip()) if qtxt else None

    def login(self):
        try:
            login_url = f"{self.BASE_URL}/ints/login"
            signin_url = f"{self.BASE_URL}/ints/signin"

            resp = self.session.get(login_url, timeout=10)
            capt = self._solve_captcha(resp.text)
            if capt is None:
                print("[!] CAPTCHA missing.")
                return False

            payload = {"username": self.username, "password": self.password, "capt": str(capt)}
            headers = {
                "Referer": login_url,
                "Origin": self.BASE_URL,
                "User-Agent": "Mozilla/5.0"
            }

            resp2 = self.session.post(signin_url, data=payload, headers=headers, timeout=10)
            self.logged_in = "Logout" in resp2.text  # crude check for success
            return self.logged_in
        except Exception as e:
            print("[!] Login error:", e)
            return False

    def number_exists(self, number_to_check: str) -> bool:
        """Check if a number exists in recent SMSCDR logs."""
        if not self.logged_in:
            if not self.login():
                raise RuntimeError("Login failed")

        data_url = f"{self.BASE_URL}/ints/client/res/data_smscdr.php"

        from_time = datetime.now() - timedelta(hours=3, minutes=1)
        to_time = datetime.now()

        params = {
            "fdate1": from_time.strftime("%Y-%m-%d %H:%M:%S"),
            "fdate2": to_time.strftime("%Y-%m-%d %H:%M:%S"),
            "iDisplayLength": "3",
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": f"{self.BASE_URL}/ints/client/SMSCDRStats"
        }

        try:
            resp = self.session.get(data_url, params=params, headers=headers, timeout=1)
            data = resp.json().get("aaData", [])
            for row in data:
                # print("[*] Checking row:", row)
                if len(row) >= 3 and row[2] == number_to_check:
                    return True
            return False
        except Exception as e:
            print("[!] Fetch error:", e)
            return True


if __name__ == "__main__":
    client = IMSClient()
    if client.number_exists("50244905584"):
        print("Number found!")
    else:
        print("Number not found.")
