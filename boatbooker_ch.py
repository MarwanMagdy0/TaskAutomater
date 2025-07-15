from playwright.sync_api import sync_playwright
import json
import time
import os

# Path to unpacked Browsec extension
EXTENSION_PATH = os.path.abspath("/home/marwan/Downloads/Browsec")

# Create a folder to store browser user data
USER_DATA_DIR = os.path.abspath("user_data")

VERIFY_BUTTON_SELECTOR = 'xpath=//*[@id="profile-control"]/div/div/div/div[2]/form/div/div[4]/div/div/div[2]/button'
PHONE_SELECTOR = 'xpath=//*[@id="phone"]'
SAVE_CHANGES_SELECTOR = 'xpath=//*[@id="profile-control"]/div/div/div/div[3]/button[1]'
OK_BUTTON_SELECTOR = 'xpath=/html/body/div[7]/div[7]/div/button'

# List of phone numbers to loop through
phone_numbers = [
    50232682960, 50231169628, 50248207388, 50237051328, 50233417740,
    50257342083, 50246149240, 50231197267, 50240388246, 50230127125,
    50253807791, 50231769851, 50253099688, 50231888179, 50253605178,
    50233907270, 50239053218, 50246210589, 50237051229, 50230307852,
    50232700212, 50230760079, 50231852144, 50232567168, 50248260906,
    50247940753, 50250052963, 50232407688, 50249387449, 50233120950,
    50248138493, 50231146557, 50240032952, 50258194059, 50252030210,
    50230307855, 50246239617, 50245885571, 50249820390, 50231378258,
    50232200998, 50253268518, 50240352082, 50259906298, 50239082404,
    50246667326, 50253842084, 50250685767, 50244904189, 50233725019
]


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

    while True:
        for number in phone_numbers:
            try:
                # Wait and clear phone field
                time.sleep(30)
                page.wait_for_selector(PHONE_SELECTOR, timeout=10000)
                phone_locator = page.locator(PHONE_SELECTOR)
                phone_locator.click()
                phone_locator.press('Control+A')
                phone_locator.press('Backspace')
                phone_locator.type(f"+{number}")
                print(f"Phone number set to: {number}")

                # Save changes
                page.locator(SAVE_CHANGES_SELECTOR).click()
                print("Save changes clicked")

                # Wait for confirmation
                page.wait_for_selector("text=Profile successfully saved!", timeout=10000)
                print("Profile saved successfully")

                # Click verify
                page.locator(VERIFY_BUTTON_SELECTOR).click()
                print("Verify button clicked")

                # Wait for OK dialog and click it
                page.wait_for_selector(OK_BUTTON_SELECTOR, timeout=10000)
                print("OK button is now visible")
                time.sleep(1)
                page.locator(OK_BUTTON_SELECTOR).click()
                print("OK button clicked")

                # Wait for Verify dialog again and close
                page.wait_for_selector("text=Verify Phone Number", timeout=10000)
                time.sleep(1)
                page.keyboard.press("Escape")
                print("Escape pressed to close the dialog")

            except Exception as e:
                print(f"❌ Error with number {number}: {e}")
                time.sleep(2)

        print("✅ Completed one full cycle of all numbers. Restarting...\n")
