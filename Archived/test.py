#!/usr/bin/env python3
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def solve_captcha(text):
    """Extract and evaluate the CAPTCHA expression."""
    match = re.search(r'What is (.+?)=', text)
    return eval(match.group(1).strip()) if match else None


def fetch_value_and_sms_data():
    try:
        # Initialize session
        session = requests.Session()
        base_url = "http://45.82.67.20"
        login_url = f"{base_url}/ints/login"
        signin_url = f"{base_url}/ints/signin"
        data_url = f"{base_url}/ints/client/res/data_smscdr.php"

        # ───── Step 1: Solve CAPTCHA ─────
        login_page = session.get(login_url, timeout=10)
        soup = BeautifulSoup(login_page.text, "html.parser")
        captcha_div = next((div.get_text(strip=True)
                            for div in soup.find_all("div", class_="col-sm-6")
                            if "What is" in div.text and "=" in div.text), None)
        captcha_answer = solve_captcha(captcha_div)

        # ───── Step 2: Login ─────
        login_payload = {
            "username": "mohamedmagdy",
            "password": "mohamedmagdy",
            "capt": str(captcha_answer)
        }
        login_headers = {
            "Referer": login_url,
            "Origin": base_url,
            "User-Agent": "Mozilla/5.0"
        }

        login_response = session.post(signin_url, data=login_payload,
                                      headers=login_headers, timeout=10)

        # ───── Step 3: Extract Dashboard Value ─────
        dashboard = BeautifulSoup(login_response.text, "html.parser")
        value_tag = dashboard.find("h4", class_="fs-20 fw-bold mb-1 text-fixed-white")
        main_value = value_tag.get_text(strip=True) if value_tag else "???"
        print("Value:", main_value)

        # ───── Step 4: Query SMSCDR Data ─────
        from_time = datetime.now() - timedelta(minutes=60*3 + 30) # 3h as time in ims is not synced
        to_time = datetime.now() 

        smscdr_params = {
            "fdate1": from_time.strftime("%Y-%m-%d %H:%M:%S"),
            "fdate2": to_time.strftime("%Y-%m-%d %H:%M:%S"),
            "iDisplayLength": "25",
        }

        ajax_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Referer": f"{base_url}/ints/client/SMSCDRStats"
        }

        smscdr_response = session.get(data_url, params=smscdr_params,headers=ajax_headers, timeout=10)

        print("Cookies:", session.cookies.get_dict())
        print("Status:", smscdr_response.status_code)
        # print("Response:\n", smscdr_response.json()["aaData"])
        for key in smscdr_response.json()["aaData"][:-1]:
            print(key[0:3])

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    fetch_value_and_sms_data()
