from playwright.sync_api import sync_playwright
from utiles import EmailManager, NumbersManager, time_logg
from web_automater_utiles import wait_for_selector, click_element, fill_input
from ims_client import IMSClient
import time, json
import os

ims_client = IMSClient()
numbers_manager = NumbersManager()


while True:
    email_id, email, cookies, log_count, remaining_emails = EmailManager.get_email_cookies_by_status()
    if email is None:
        time_logg("No available email found.")
        break

    print(f"* [{email}] Using email: {email}, log count: {log_count}, remaining emails: {remaining_emails}")
    with sync_playwright() as p:
        number_id, number = numbers_manager.get_available_number()
        print(f"Using number: {number}")
        browser = p.chromium.launch(headless=False)
        # context = p.chromium.launch_persistent_context(
        #     "Browser_Data/user_data2",
        #     headless=False,
        #     args=[
        #         f"--disable-extensions-except=Browser_Data/Browsec",
        #         f"--load-extension=Browser_Data/Browsec",
        #     ]
        # )
        context = browser.new_context()
        # Step 2: Set cookies to the context
        context.add_cookies(json.loads(cookies))

        # Step 3: Open page with those cookies
        page = context.new_page()
        page.wait_for_timeout(1000)  # Wait for 1 seconds to ensure the page is fully loaded
        while True:
            try:
                page.goto("https://app.bitly.com/settings/profile", wait_until="load")
                print("Page loaded with cookies.")
                break
            except Exception as e:
                print(f"Error loading page: {e}")
                time.sleep(1)
        
        page.select_option("#two-factor-country-code", label="Guatemala (+502)")

        page.fill('#profile-mobile-number', number[3:])  # Replace with desired number
        # Click the send button
        page.click("button:has-text('Send verification code')", timeout=60000)
        time_logg("Send verification code")
        page.wait_for_timeout(100000)