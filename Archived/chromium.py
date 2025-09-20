from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import sys

if len(sys.argv) == 1:
    sys.argv.append("")

def run():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="Browser_Data/user_data0",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ],
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9"
            }
        )

        page = context.pages[0] if context.pages else context.new_page()
        stealth_sync(page)

        page.goto("https://fishingbooker.com/web/manage/account", wait_until="load")

        print("✅ Page loaded. Waiting for iframe...")

        # Wait for the iframe to appear
        iframe_element = page.wait_for_selector("iframe", timeout=10000)
        iframe = iframe_element.content_frame()

        if iframe is None:
            print("❌ Failed to access iframe content")
        else:
            print("✅ Iframe loaded successfully")

            # Optional: take a screenshot of iframe
            iframe.screenshot(path="iframe.png")
            
            # You can also inspect its content or fill in fields
            # Example:
            # iframe.fill('input[name="fm-login-id"]', "your_username")

        # Keep window open
        page.wait_for_timeout(1000000000)
        context.close()

if __name__ == "__main__":
    run()
