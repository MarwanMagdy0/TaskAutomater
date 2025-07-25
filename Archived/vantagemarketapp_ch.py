from playwright.sync_api import sync_playwright
from web_automater_utiles import wait_for_selector, CaptchaViewer
from utiles import PhoneStatusManager, time_logg
from ims_client import IMSClient
import json
import time
import os


# Path to unpacked Browsec extension
EXTENSION_PATH = os.path.abspath("Browsec")
viewer = CaptchaViewer()

# Create a folder to store browser user data
USER_DATA_DIR = os.path.abspath(f"user_data")

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
    
    page.goto("https://webh5.vantagemarketapp.com/app-web/ads-put-wta/?rt=Growth_PerformanceMKT_Google_UG&gad_source=1&gad_campaignid=22759316544")
    Err_happened = False
    
    # page.on("request", intercept_request)
    
    while True:
        if not Err_happened:
            number = manager.get_next_number_status()

        time_logg(f"Current number to process: {number}")
        if number is None:
            time_logg("No numbers available to process. Exiting...")
            break
        try:
            # if wait_for_selector(page, '//*[@id="mobile"]', timeout=60000):
            if wait_for_selector(page, '//*[@id="first_name"]', timeout=60000):
                page.fill('//*[@id="first_name"]', "Sample Text")
            
            if wait_for_selector(page, '//*[@id="last_name"]', timeout=60000):
                page.fill('//*[@id="last_name"]', "Sample Last Name")
            
            if wait_for_selector(page, '//*[@id="email"]', timeout=60000):
                page.fill('//*[@id="email"]', "sample@example.com")
            
            if wait_for_selector(page, '//*[@id="password"]', timeout=60000):
                page.fill('//*[@id="password"]', "abcABC123!@#")

            if wait_for_selector(page, '//*[@id="confirm_password"]', timeout=60000):
                page.fill('//*[@id="confirm_password"]', "abcABC123!@#")
            
            print("waiting for phone input")
            if wait_for_selector(page, 'body > section:nth-child(4) > div > div > div.right-box > div > section > div > div.form-body > div.phone_box > div.mobile_box > div.form_input.country_dropdown', timeout=60000):
                time_logg("Element is visible and ready to be interacted with.")
                page.click('body > section:nth-child(4) > div > div > div.right-box > div > section > div > div.form-body > div.phone_box > div.mobile_box > div.form_input.country_dropdown')

            if wait_for_selector(page, '//*[@id="UZ"]', timeout=60000):
                page.click('//*[@id="UZ"]')
                time_logg("Clicked on the Uzbekistan element.")
            
            if wait_for_selector(page, '//*[@id="phone_number"]', timeout=60000):
                page.fill('//*[@id="phone_number"]', "951206542")
                time_logg(f"Filled phone number: {number}")

            if wait_for_selector(page, '//*[@id="getVerifyCode"]', timeout=60000):
                page.click('//*[@id="getVerifyCode"]')
                time_logg("Clicked on the 'Get Verify Code' button.")
            
            page.wait_for_selector('xpath=//*[@id="captcha"]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]')

            # Now extract the image src inside this container
            img_element = page.query_selector('xpath=//*[@id="captcha"]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]//img')
            if img_element:
                img_src = img_element.get_attribute("src")
                viewer.update_image(img_src)

            if ims_client.number_exists(number):
                time_logg(f"Number {number} exists in IMS logs.")
                manager.update_number_status(number, is_working=True)
            else:
                time_logg(f"Number {number} does not exist in IMS logs.")
                manager.update_number_status(number, is_working=False)
            Err_happened = False
            time_logg("Reloading the webpage...")
            page.wait_for_selector('text=Request again', timeout=60000)
            page.reload()

        except Exception as e:
            Err_happened = True
            time_logg(f"❌ Error with number {number}: {e}")
            time.sleep(2)

