from playwright.sync_api import sync_playwright
from utiles import PhoneStatusManager, EmailManager, time_logg
from web_automater_utiles import wait_for_selector, click_element, fill_input
from ims_client import IMSClient
import time, json
import os

phone_manager = PhoneStatusManager("numbers.json")
ims_client = IMSClient()
# List all files in the directory
directory = "tradingview_cookies_new"
files = os.listdir(directory)[21:]
print("Files in directory:", files)
for idx, cookies_file in enumerate(files):
    print(f"[{idx:02}] Processing file: {cookies_file}")
    with sync_playwright() as p:
        number = phone_manager.get_next_number_status()
        print(f"Using number: {number}")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Step 1: Load cookies from file
        with open(os.path.join(directory, cookies_file), "r") as f:
            cookies = json.load(f)

        # Step 2: Set cookies to the context
        context.add_cookies(cookies)

        # Step 3: Open page with those cookies
        page = context.new_page()
        page.goto("https://ar.tradingview.com/settings/#account-settings")
        try:
            page.wait_for_selector("text=Add phone", timeout=240000)
            page.click("text=Add phone")
            time.sleep(2)  # Wait for the dialog to appear
            if not click_element(page, '//*[@id=":ro:"]', timeout=500):
                if not click_element(page, '//*[@id=":rt:"]', timeout=500):
                    click_element(page, '//*[@id=":rg:"]', timeout=500)

            page.wait_for_selector("text=موزانبيق", timeout=240000)
            page.click("text=موزانبيق")

            if not fill_input(page, '//*[@id=":rf:"]', f"{number}"[3:], timeout=1000):
                fill_input(page, '//*[@id=":rn:"]', f"{number}"[3:], timeout=1000)

            time.sleep(1)

            page.click("text=احصل على الرمز")
            if wait_for_selector(page, "text=يبدو أنك حاولت التحقق من رقم هاتفك عدة مرات. عد غدًا للمحاولة مرة أخرى.", timeout=5000):
                print("Too many attempts")
            else:
                if wait_for_selector(page, "text=لقد أرسلنا الرمز", timeout=240000):
                    print("Verify your phone number dialog appeared.")
                    time.sleep(4)
                    if ims_client.number_exists(number):
                        time_logg(f"Number {number} exists in IMS logs.")
                        phone_manager.update_number_status(number, is_working=True)
                    else:
                        time_logg(f"Number {number} does not exist in IMS logs.")
                        phone_manager.update_number_status(number, is_working=False)
            
            page.wait_for_timeout(60000)  # Wait for 5 seconds to ensure the page is fully loaded
            browser.close()
        except Exception as e:
            time_logg(f"An error occurred: {e}")
            browser.close()