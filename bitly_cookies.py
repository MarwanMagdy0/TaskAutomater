from playwright.sync_api import sync_playwright
from utiles import EmailManager, NumbersManager, time_logg
from web_automater_utiles import wait_for_selector, click_element, fill_input
from ims_client import IMSClient
import time, json
import os, sys
from tqdm import tqdm

ims_client = IMSClient()
numbers_manager = NumbersManager("database/bitly_database.db")

sleep_time = 30 # Minuits
total_seconds = int(60 * sleep_time)
email_manager = EmailManager("database/bitly_database.db")

# print(f"waiting {total_seconds} seconds...")
# for _ in tqdm(range(total_seconds), desc="Progress", ncols=70):
#     time.sleep(1)
email_id, email, cookies, log_count = email_manager.get_least_and_oldest_email()
if email is None:
    time_logg("No available email found.")
    sys.exit(1)

print(f"[*] {email} Using email: {email}, log count: {log_count}")
with sync_playwright() as p:
    number_id, number = numbers_manager.get_available_number()
    print(number)
    print(f"Using number: {number}")
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    context.add_cookies(json.loads(cookies))
    page = context.new_page()
    page.wait_for_timeout(1000)
    while True:
        try:
            page.goto("https://app.bitly.com/settings/profile", wait_until="load")
            print("Page loaded with cookies.")
            break
        except Exception as e:
            print(f"Error loading page: {e}")
            time.sleep(1)
    
    try:
        # Senegal (+221)
        # Guatemala (+502)
        page.select_option("#two-factor-country-code", label="Senegal (+221)")
        page.fill('#profile-mobile-number', number[3:])  # Replace with desired number
        page.wait_for_timeout(1000)
        page.click("button:has-text('Send verification code')", timeout=60000)
        time_logg("Send verification code")

        # A verification code has been sent to your phone
        # Failed to set phone number

        while True:
            if wait_for_selector(page, "text=verification code has been sent", timeout=100):
                page.wait_for_timeout(3000)
                numbers_manager.check_number(number_id, number)
                email_manager.log_status(email, "CODE_SENT")
                break
            elif wait_for_selector(page, "text=Failed to set phone number", timeout=100):
                email_manager.log_status(email, "Failed")
                break

    except Exception as e:
        print(f"Error : {e}")
