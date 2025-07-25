from playwright.sync_api import sync_playwright
from utiles import PhoneStatusManager, FileManager, time_logg
from web_automater_utiles import wait_for_selector, click_element, fill_input
from ims_client import IMSClient
import time, json
import os

phone_manager = PhoneStatusManager("numbers.json")
ims_client = IMSClient()
file_manager = FileManager("emails.json")
# List all files in the directory
directory = "tradingview_cookies_23_7"
files = os.listdir(directory)
print("Files in directory:", files)
for idx, cookies_file in enumerate(files):
    frequency = file_manager.get_frequency(os.path.join(directory, cookies_file))
    if frequency > 10:
        print(f"Skipping {cookies_file} as it has {frequency} triggers.")
        continue

    print(f"[{idx:02}] Processing file: {cookies_file}")
    with sync_playwright() as p:
        number = phone_manager.get_next_number_status()
        print(f"Using number: {number}")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Step 1: Load cookies from file
        with open(os.path.join(directory, cookies_file), "r") as f:
            cookies = json.load(f)

        # Step 2: Set cookies to the context
        context.add_cookies(cookies)

        # Step 3: Open page with those cookies
        page = context.new_page()
        page.wait_for_timeout(1000)  # Wait for 1 seconds to ensure the page is fully loaded
        while True:
            try:
                page.goto("https://ar.tradingview.com/settings/#account-settings", wait_until="load")
                print("Page loaded with cookies.")
                break
            except Exception as e:
                print(f"Error loading page: {e}")
                time.sleep(1)
        try:
            page.wait_for_selector("text=Add phone", timeout=240000)
            page.click("text=Add phone")
            time.sleep(2)  # Wait for the dialog to appear
            dropdown_button = page.locator('button[role="combobox"][aria-labelledby="country-select-id"]')
            dropdown_button.wait_for(state="visible", timeout=10000)
            dropdown_button.click()

            page.wait_for_selector("text=موزانبيق", timeout=240000)
            page.click("text=موزانبيق")
            
            phone_input = page.locator('input[data-qa-id="ui-lib-Input-input"]')
            phone_input.wait_for(state="visible", timeout=10000)
            phone_input.fill(f"{number}"[3:])

            time.sleep(1)

            page.click("text=احصل على الرمز")
            if wait_for_selector(page, "text=يبدو أنك حاولت التحقق من رقم هاتفك عدة مرات. عد غدًا للمحاولة مرة أخرى.", timeout=5000):
                print("Too many attempts")
            else:
                if wait_for_selector(page, "text=لقد أرسلنا الرمز", timeout=240000):
                    file_manager.log_trigger(os.path.join(directory, cookies_file))
                    print("Verify your phone number dialog appeared.")
                    time.sleep(1)
                    if ims_client.number_exists(number):
                        time_logg(f"Number {number} exists in IMS logs.")
                        phone_manager.update_number_status(number, is_working=True)
                    else:
                        time_logg(f"Number {number} does not exist in IMS logs.")
                        phone_manager.update_number_status(number, is_working=False)
            
            page.wait_for_timeout(500)  # Wait for 5 seconds to ensure the page is fully loaded
            browser.close()
        except Exception as e:
            time_logg(f"An error occurred: {e}")
            browser.close()
            