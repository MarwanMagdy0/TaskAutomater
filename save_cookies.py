from playwright.sync_api import sync_playwright
import json
import time
import sys

if len(sys.argv) < 2:
    print("Usage: python load_cookies.py <cookies_file>")
    sys.exit(1)

file_name = sys.argv[1].split('@')[0]

cookies_file = f"tradingview_cookies_new/{file_name}.json"

print(file_name)
print(cookies_file)
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://ar.tradingview.com/pricing/?source=account_activate&feature=redirect")  # 🔐 Replace with your URL

        print("🔄 Waiting for you to interact with the page...")

        try:
            while True:
                try:
                    _ = page.title()  # Try to access title
                except Exception:
                    print("❌ Page closed.")
                    break
                time.sleep(1)  # Wait before checking again
        except KeyboardInterrupt:
            print("❌ Interrupted manually.")

        print("💾 Saving cookies...")
        state = context.storage_state()
        cookies = state.get("cookies", [])

        with open(cookies_file, "w") as f:
            json.dump(cookies, f, indent=2)

        print("✅ Cookies saved to cookies.json")
        input("Press Enter to close the browser...")
        browser.close()

if __name__ == "__main__":
    main()
