from playwright.sync_api import sync_playwright
import json
import time
import os

# Path to unpacked Browsec extension
EXTENSION_PATH = os.path.abspath("Browsec")

# Create a folder to store browser user data
USER_DATA_DIR = os.path.abspath("user_data")

VERIFY_BUTTON_SELECTOR = 'xpath=//*[@id="profile-control"]/div/div/div/div[2]/form/div/div[4]/div/div/div[2]/button'
PHONE_SELECTOR = 'xpath=//*[@id="phone"]'
SAVE_CHANGES_SELECTOR = 'xpath=//*[@id="profile-control"]/div/div/div/div[3]/button[1]'

# List of phone numbers to loop through
phone_numbers = [
    50246667326, 50239082404, 50253842084, 50250685767, 50232682960, 50233725019, 50253605178, 50231769851, 50253807791, 258826466671, 258828771634, 50231197267, 50246149240, 50233417740, 50248207388
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
                ok_button = page.get_by_role("button", name="OK")
                if ok_button.count() > 0 and ok_button.first.is_visible():
                    ok_button.first.click()
                    print("OK button clicked")
                else:
                    print("No visible OK button found")

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
