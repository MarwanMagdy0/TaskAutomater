from playwright.sync_api import sync_playwright
import os, sys

# Check if sys.argv[1] exists, otherwise set it to an empty string
if len(sys.argv) == 1:
    sys.argv.append("")

# Path to unpacked Browsec extension
# EXTENSION_PATH = os.path.abspath("Browsec")

# # Create a folder to store browser user data
# USER_DATA_DIR = os.path.abspath(f"user_data{sys.argv[1]}")

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto("https://cnlogin.cainiao.com/register?redirectURL=https%3A%2F%2Fwww.cainiao.com%2Fen%2Findex.html&cnSite=CAINIAO&bizSource=&showcn=true&lang=en_US")  # Open any URL you want
        print("Opened Chromium and navigated to https://app.staffany.com/login?origin=/")
        page.wait_for_timeout(1000000000)  # Wait 10 seconds so you can see it
        browser.close()

if __name__ == "__main__":
    run()
