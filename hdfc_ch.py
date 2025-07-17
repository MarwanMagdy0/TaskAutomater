from playwright.sync_api import sync_playwright
from utiles import PhoneStatusManager, time_logg
from ims_client import IMSClient
import json
import time
import os
import sys

# xdotool key Caps_Lock

# Check if sys.argv[1] exists, otherwise set it to an empty string
if len(sys.argv) == 1:
    sys.argv.append("")

# Path to unpacked Browsec extension
EXTENSION_PATH = os.path.abspath("Browsec")

# Create a folder to store browser user data
USER_DATA_DIR = os.path.abspath(f"user_data{sys.argv[1]}")

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
    page.goto("https://netportal.hdfcbank.com/login")
    Err_happened = False

    page.wait_for_selector('//*[@id="forgotCustId"]', timeout=10000)
    page.click('//*[@id="forgotCustId"]')
    while True:
        if not Err_happened:
            number = manager.get_next_number_status()

        time_logg(f"Current number to process: {number}")
        if number is None:
            time_logg("No numbers available to process. Exiting...")
            break
        
        try:
            # Select all and clear the input field, then type the number
            mobile_input = page.wait_for_selector('//*[@id="custMobileNo"]', timeout=60000)
            mobile_input.fill("")  # Clear the input field
            time.sleep(0.5)  # Wait for the field to clear
            mobile_input.type(f"+{number}")  # Type the number
            time_logg(f"✅ Entered mobile number {number}")

            while True:
                id_input = page.wait_for_selector('//*[@id="id"]', timeout=60000)
                id_input.click(force=True)
                id_value = id_input.input_value()
                if len(id_value) == 6:
                    # Wait for the "CONTINUE" link to appear and click it
                    continue_link = page.wait_for_selector('//a[text()="CONTINUE"]', timeout=60000)
                    continue_link.click()
                    time_logg(f"✅ Clicked on 'CONTINUE' link for number {number}")
                    break
                    otp_input = page.locator('//*[@id="mobileOtp"]')
                    if otp_input.wait_for(timeout=60000, state="visible"):
                        break
                time.sleep(0.5)  # Poll every 0.5 seconds
            
            # Wait for the OTP input field to appear and type the OTP
            otp_input = page.wait_for_selector('//*[@id="mobileOtp"]', timeout=60000)
            otp_input.fill("")  # Clear the input field
            time.sleep(0.5)  # Wait for the field to clear
            otp_input.type("123456")  # Type the OTP
            time_logg(f"✅ Entered OTP 123456 for number {number}")

            # Wait for the "CONTINUE" link to appear and click it
            otp_continue_link = page.wait_for_selector('//a[text()="CONTINUE"]', timeout=60000)
            otp_continue_link.click()
            time_logg(f"✅ Clicked on 'CONTINUE' link after entering OTP for number {number}")

            # Wait for the "DONE" button to appear and click it
            done_button = page.wait_for_selector('//a[text()="DONE"]', timeout=60000)
            done_button.click()
            time_logg(f"✅ Clicked on 'DONE' button for number {number}")

            mobile_input = page.wait_for_selector('//*[@id="custMobileNo"]', timeout=60000) # WAIT for the input to be available again
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
