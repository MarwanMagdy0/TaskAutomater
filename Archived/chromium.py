from playwright.sync_api import sync_playwright
import os, sys

# Check if sys.argv[1] exists, otherwise set it to an empty string
if len(sys.argv) == 1:
    sys.argv.append("")

# Path to unpacked Browsec extension
EXTENSION_PATH = os.path.abspath("Browsec")

# Create a folder to store browser user data
USER_DATA_DIR = os.path.abspath(f"user_data{sys.argv[1]}")

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            headless=False,
            args=[
                f"--disable-extensions-except={EXTENSION_PATH}",
                f"--load-extension={EXTENSION_PATH}",
            ]
        ) # Set headless=True if you don't want a window
        page = browser.pages[0] if browser.pages else browser.new_page()
        page.goto("https://app.staffany.com/login?origin=/")  # Open any URL you want
        print("Opened Chromium and navigated to https://app.staffany.com/login?origin=/")
        page.wait_for_timeout(1000000000)  # Wait 10 seconds so you can see it
        browser.close()

if __name__ == "__main__":
    run()
