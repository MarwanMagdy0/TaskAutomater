import re
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


class IMSClient:
    BASE_URL = "http://45.82.67.20"

    def __init__(self, username="MohamedMagdy1", password="MohamedMagdy1"):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            )
        })
        self.username = username
        self.password = password
        self.logged_in = False

    # ─────────────── helpers ───────────────
    @staticmethod
    def _solve_captcha_from_html(html: str) -> int:
        """
        Extracts and solves the math captcha: "What is A (+-*/) B ="
        Returns integer result. Raises ValueError if not found/parseable.
        """
        soup = BeautifulSoup(html, "html.parser")
        # The question lives in <div class="col-sm-6"> ... "What is 1 + 2 ="
        for d in soup.find_all("div", class_="col-sm-6"):
            t = d.get_text(" ", strip=True)
            m = re.search(r'What\s+is\s+(\d+)\s*([+\-*/])\s*(\d+)', t, flags=re.I)
            if m:
                a = int(m.group(1))
                op = m.group(2)
                b = int(m.group(3))
                if op == '+':
                    return a + b
                elif op == '-':
                    return a - b
                elif op == '*':
                    return a * b
                elif op == '/':
                    return a // b if b != 0 else 0
        raise ValueError("Captcha not found")

    @staticmethod
    def _find_etkk(html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        etkk = soup.find("input", {"name": "etkk"})
        return etkk["value"].strip() if etkk and etkk.has_attr("value") else ""

    # ─────────────── auth ───────────────
    def login(self) -> bool:
        """
        Login using math captcha (+ optional etkk). Verifies success by loading Dashboard.
        """
        try:
            login_url = f"{self.BASE_URL}/ints/login"
            signin_url = f"{self.BASE_URL}/ints/signin"
            dashboard_url = f"{self.BASE_URL}/ints/client/SMSDashboard"

            # 1) Load login → parse captcha (+ etkk if present)
            r1 = self.session.get(login_url, timeout=15)
            r1.raise_for_status()

            capt = self._solve_captcha_from_html(r1.text)
            etkk_value = self._find_etkk(r1.text)

            # 2) Sign in
            payload = {
                "username": self.username,
                "password": self.password,
                "capt": str(capt),
            }
            if etkk_value:
                payload["etkk"] = etkk_value

            headers = {
                "Referer": login_url,
                "Origin": self.BASE_URL,
                "User-Agent": self.session.headers["User-Agent"],
            }
            r2 = self.session.post(
                signin_url,
                data=payload,
                headers=headers,
                allow_redirects=True,
                timeout=20,
            )
            r2.raise_for_status()

            # 3) Verify by loading dashboard page
            r3 = self.session.get(dashboard_url, timeout=20)
            r3.raise_for_status()

            # A simple robust check: page contains the SMS dashboard title string
            self.logged_in = "IMS SMS | SMS Dashboard" in r3.text or "SMS Dashboard" in r3.text
            return self.logged_in

        except Exception as e:
            print("[!] Login error:", e)
            self.logged_in = False
            return False

    # ─────────────── data ───────────────
    def number_exists(self, number_to_check: str) -> bool:
        """
        Check if a number exists in recent SMSCDR logs (last ~3h).
        Returns True if found; False if not found or on fetch failure after login succeeds.
        Raises RuntimeError if login fails.
        """
        if not self.logged_in:
            if not self.login():
                raise RuntimeError("Login failed")

        data_url = f"{self.BASE_URL}/ints/client/res/data_smscdr.php"

        from_time = datetime.now() - timedelta(hours=3, minutes=1)
        to_time = datetime.now()

        params = {
            "fdate1": from_time.strftime("%Y-%m-%d %H:%M:%S"),
            "fdate2": to_time.strftime("%Y-%m-%d %H:%M:%S"),
            "iDisplayLength": "50",  # look at more rows to be safer
        }

        headers = {
            "User-Agent": self.session.headers["User-Agent"],
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": f"{self.BASE_URL}/ints/client/SMSCDRStats",
        }

        try:
            resp = self.session.get(data_url, params=params, headers=headers, timeout=10)
            resp.raise_for_status()
            aa = (resp.json() or {}).get("aaData", []) or []
            # Compare as strings; normalize whitespace just in case
            target = str(number_to_check).strip()
            for row in aa:
                if len(row) >= 3 and str(row[2]).strip() == target:
                    return True
            return False
        except Exception as e:
            print("[!] Fetch error:", e)
            # We already authenticated; a transient fetch error should not claim the number exists.
            return False


if __name__ == "__main__":
    client = IMSClient()
    try:
        found = client.number_exists("50244905584")
        print("Number found!" if found else "Number not found.")
    except RuntimeError as e:
        print(str(e))
