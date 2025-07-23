import json
from playwright.sync_api import sync_playwright
import sys

if len(sys.argv) < 2:
    print("Usage: python load_cookies.py <cookies_file>")
    sys.exit(1)

cookies_file = f"tradingview_cookies_23_7/{sys.argv[1]}.json"
target_url = "https://ar.tradingview.com/settings/#account-settings"  # Or wherever your cookies belong
print(cookies_file)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Step 1: Load cookies from file
    with open(cookies_file, "r") as f:
        cookies = json.load(f)

    # Step 2: Set cookies to the context
    context.add_cookies(cookies)

    # Step 3: Open page with those cookies
    page = context.new_page()
    page.goto(target_url)

    print("Page loaded with cookies.")
    input("Press Enter to close the browser...")
    browser.close()
