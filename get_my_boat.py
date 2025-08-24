# pip install playwright faker
# playwright install

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeoutError
from faker import Faker
import time
import pathlib
import sys

fake = Faker()

# ----------------- Helpers -----------------
def wait_for_selector(page, selector, timeout_ms=15000, state="visible"):
    try:
        page.wait_for_selector(selector, timeout=timeout_ms, state=state)
        return True
    except PWTimeoutError:
        return False

def safe_click(page, selector, timeout_ms=15000, state="visible"):
    if wait_for_selector(page, selector, timeout_ms, state):
        page.locator(selector).click()
        return True
    return False

def safe_fill(page, selector, value, timeout_ms=15000):
    if wait_for_selector(page, selector, timeout_ms, "editable"):
        page.fill(selector, value)
        return True
    return False

def screenshot(page, label):
    out = pathlib.Path("debug_screens")
    out.mkdir(exist_ok=True)
    path = out / f"{int(time.time())}_{label}.png"
    page.screenshot(path=str(path), full_page=True)
    print(f"[debug] saved {path}")

# ----------------- Main flow -----------------
def run_flow(base_url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                # Keep flags minimal so the window stays responsive
                "--disable-blink-features=AutomationControlled"
            ],
        )

        # No stealth, no proxy sites, no cookie juggling
        context = browser.new_context(
            viewport={"width": 1366, "height": 768},
            device_scale_factor=1.0,
            is_mobile=False,
            has_touch=False,
            locale="en-US",
            timezone_id="UTC",
            # Let Playwright set UA; override only if your QA plan requires it
        )
        page = context.new_page()

        # See JS console output and runtime errors that often cause “frozen UI”
        page.on("console", lambda m: print(f"PAGE {m.type}: {m.text}"))
        page.on("pageerror", lambda e: print("PAGE ERROR:", e))

        page.set_default_timeout(20000)

        print(f"[info] Navigating to {base_url}")
        page.goto(base_url)

        # Optional: open the Inspector so you can interact manually while debugging
        # page.pause()

        try:
            # ------- Replace the selectors below with your OWN app’s selectors -------
            # Example “open menu” (robust role/text query)
            safe_click(page, 'button:has-text("Menu")', 5000)

            # Example “open sign up”
            safe_click(page, 'a:has-text("Sign up")', 8000)

            # Example form fill (use test accounts on your staging environment)
            safe_fill(page, 'input[placeholder="First name"]', fake.first_name())
            safe_fill(page, 'input[placeholder="Last name"]', fake.last_name())
            safe_fill(page, 'input[type="email"]', f"qa+{int(time.time())}@example.com")
            safe_fill(page, 'input[type="password"]', "ChangeMe!12345")

            # Example submit
            if safe_click(page, 'button:has-text("Create Account")', 8000):
                print("[info] submitted form")

            # Take an artifact at the end
            screenshot(page, "end_of_flow")

        except Exception as e:
            screenshot(page, "exception")
            print(f"[error] Exception during flow: {e}", file=sys.stderr)

        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    # Use a staging URL or a site you own/are authorized to test
    run_flow("https://www.getmyboat.com")
