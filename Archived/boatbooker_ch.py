from playwright.sync_api import sync_playwright
from utiles import PhoneStatusManager, time_logg
from ims_client import IMSClient
import json
import time
import os
import sys

# Check if sys.argv[1] exists, otherwise set it to an empty string
if len(sys.argv) == 1:
    sys.argv.append("")

# Path to unpacked Browsec extension
EXTENSION_PATH = os.path.abspath("Browsec")

# Create a folder to store browser user data
USER_DATA_DIR = os.path.abspath(f"user_data{sys.argv[1]}")

VERIFY_BUTTON_SELECTOR = 'xpath=//*[@id="profile-control"]/div/div/div/div[2]/form/div/div[4]/div/div/div[2]/button'
PHONE_SELECTOR = 'xpath=//*[@id="phone"]'
SAVE_CHANGES_SELECTOR = 'xpath=//*[@id="profile-control"]/div/div/div/div[3]/button[1]'
OK_BUTTON_SELECTOR = 'body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button'

manager = PhoneStatusManager("numbers.json")
ims_client = IMSClient()

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,
        args=[
            f"--disable-extensions-except={EXTENSION_PATH}",
            f"--load-extension={EXTENSION_PATH}",
        ]
    )

    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://boatbooker.com/manage/profile")
    Err_happened = False
    while True:
        if not Err_happened:
            number = manager.get_next_number_status()

        time_logg(f"Current number to process: {number}")
        if number is None:
            time_logg("No numbers available to process. Exiting...")
            break
        page.keyboard.press("Escape")
        try:
            # Wait and clear phone field
            time.sleep(30)
            page.keyboard.press("Escape")
            page.wait_for_selector(PHONE_SELECTOR, timeout=10000)
            phone_locator = page.locator(PHONE_SELECTOR)
            phone_locator.click()
            phone_locator.press('Control+A')
            phone_locator.press('Backspace')
            phone_locator.type(f"+{number}")
            time_logg(f"Phone number set to: {number}")

            # Save changes
            page.locator(SAVE_CHANGES_SELECTOR).click()
            time_logg("Save changes clicked")

            # Wait for confirmation
            page.wait_for_selector("text=Profile successfully saved!", timeout=10000)
            time_logg("Profile saved successfully")

            # Click verify
            page.locator(VERIFY_BUTTON_SELECTOR).click()
            time_logg("Verify button clicked")

            # Wait for OK dialog and click it
            page.wait_for_selector(OK_BUTTON_SELECTOR, timeout=10000)
            time_logg("OK button is now visible")
            time.sleep(1)
            page.locator(OK_BUTTON_SELECTOR).click()
            time_logg("OK button clicked")

            # Wait for Verify dialog again and close
            page.wait_for_selector("text=Verify Phone Number", timeout=10000)
            page.wait_for_timeout(1000)  # Wait 1 second

            if page.locator("text=Oops, something went wrong.").is_visible():
                time_logg("Oops, something went wrong message detected")
                page.keyboard.press("Escape")
                continue

            page.keyboard.press("Escape")
            time_logg("Escape pressed to close the dialog")

            # Check if the number exists in IMS logs
            if ims_client.number_exists(number):
                time_logg(f"Number {number} exists in IMS logs.")
                manager.update_number_status(number, is_working=True)
            else:
                time_logg(f"Number {number} does not exist in IMS logs.")
                manager.update_number_status(number, is_working=False)
            
            Err_happened = False

        except Exception as e:
            Err_happened = True
            time_logg(f"❌ Error with number {number}: {e}")
            time.sleep(2)
