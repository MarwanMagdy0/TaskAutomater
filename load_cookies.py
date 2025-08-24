import sqlite3, json
from playwright.sync_api import sync_playwright
import sys

conn = sqlite3.connect('database/weltrade_database.db')
cursor = conn.cursor()
target_url = "https://secure.weltrade.com/settings/personal-data"
if len(sys.argv) < 2:
    print("Usage: python load_cookies.py <cookies_file>")
    sys.exit(1)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    cursor.execute("SELECT cookies FROM emails WHERE email = ?", (sys.argv[1],))
    cookies_row = cursor.fetchone()
    if not cookies_row:
        print(f"No cookies found for email: {sys.argv[1]}")
        sys.exit(1)
    # Step 2: Set cookies to the context
    context.add_cookies(json.loads(cookies_row[0]))

    # Step 3: Open page with those cookies
    page = context.new_page()
    page.goto(target_url)

    print("Page loaded with cookies.")
    input("Press Enter to close the browser...")
    browser.close()
