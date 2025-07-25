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
    page.goto("https://web.flypgs.com/signup?_gl=1*4y03c6*_up*MQ..*_gs*MQ..&gclid=CjwKCAjw7MLDBhAuEiwAIeXGIV69sOeq2mn4uf3Z9zW3QrudG4AG_IbBXqpC5Dcpe7vFskCpqD3xFBoCTSoQAvD_BwE&gclsrc=aw.ds&gbraid=0AAAAADscbGzQxI44Ad-8qphdJbZDSAjIp")
    Err_happened = False
    while True:
        if not Err_happened:
            number = manager.get_next_number_status()

        time_logg(f"Current number to process: {number}")
        if number is None:
            time_logg("No numbers available to process. Exiting...")
            break
        
        try:
            page.wait_for_selector('//*[@id="mui-5"]', timeout=1000000000)
            page.fill('//*[@id="mui-5"]', "Marwan")
            page.fill('//*[@id="mui-6"]', "Maroo")
            page.fill('//*[@id="mui-9"]', "email@gmail.com")
            # Click on the specified element
            page.click('//*[@id="page"]/div[3]/div/div[2]/div/form/div/div[3]/div[2]/div[3]/div[1]/label/span[1]/input')
            page.click('//*[@id="page"]/div[3]/div/div[2]/div/form/div/div[3]/div[2]/div[3]/div[2]/label/span[1]/input')
            page.click('//*[@id="page"]/div[3]/div/div[2]/div/form/div/div[3]/div[4]/label/span[1]/input')
            page.click('//*[@id="page"]/div[3]/div/div[2]/div/form/div/div[3]/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div/button/div/div[2]')
            # Wait for the text "Senegal (+221)" to appear and click it
            page.wait_for_selector("//div[text()='Senegal (+221)']", timeout=120000)
            page.click("//div[text()='Senegal (+221)']")
            page.fill('//*[@id="mui-7"]', '76')
            page.fill('//*[@id="mui-8"]', f"{number}"[5:])
            page.wait_for_selector("xpath=//*[@id='recaptcha-anchor']/div", timeout=600000)
            print("found")
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
