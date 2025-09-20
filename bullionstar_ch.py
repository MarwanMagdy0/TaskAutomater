from playwright.sync_api import sync_playwright
from utiles import NumbersManager
import time

PROFILE_PATH = "Browser_Data/user_data0"  # persistent profile
REMOVE_THRESHOLD = 0.1   # allowed range ±0.1 USD
MAX_ALERTS = 6            # maximum allowed alerts
REFRESH_DELAY = 90        # seconds between cycles

def get_spot_price(page):
    """Extract the current spot price in USD."""
    prices = page.locator("span.metals.xau").all_inner_texts()
    usd_prices = [p for p in prices if p.startswith("US$")]
    spot_text = usd_prices[-1]  # last USD entry is the per-ounce spot price
    return float(spot_text.replace("US$", "").replace(",", "").strip())


def manage_alerts(page, spot_price):
    print(f"\nSpot price: {spot_price:.2f}")

    while True:
        rows = page.locator("div.active-alert table.alert tbody tr")
        count = rows.count()
        if count == 0:
            print("No alerts found.")
            break

        removed_any = False

        for i in range(count):
            row = rows.nth(i)
            price_text = row.locator("td").nth(1).inner_text().strip()
            price_value = float(price_text.replace("US$", "").replace(",", ""))
            remove_btn = row.locator("img.remove")

            if abs(price_value - spot_price) >= REMOVE_THRESHOLD:
                print(f"❌ Removing alert {price_value:.2f} (outside ±{REMOVE_THRESHOLD})")
                remove_btn.click()
                try:
                    ok_btn = page.wait_for_selector("button.btn-common-radius.ok", timeout=3000)
                    ok_btn.click()
                except:
                    pass
                time.sleep(0.25)
                removed_any = True
                break  # break and reload rows immediately

        if not removed_any:
            break  # no more to remove, exit loop

    # Reload alerts after all removals
    rows = page.locator("div.active-alert table.alert tbody tr")
    current_count = rows.count()
    print("Remaining alerts:", current_count)

    # Add alerts if less than max
        # Add alerts if less than max
    if current_count <= MAX_ALERTS:
        needed = MAX_ALERTS - current_count
        print(f"➕ Adding {needed} alerts around {spot_price:.2f}")

        offsets = [0.01, 0.02, 0.03, -0.01, -0.02, -0.03]

        for offset in offsets[:needed]:
            new_price = spot_price + offset
            print(f"Adding alert {new_price:.2f}")
            page.locator("input.txt-decimal.price-alert-value").fill(f"{new_price:.2f}")
            page.locator("#btn-set-alert").click()
            try:
                ok_btn = page.wait_for_selector("button.btn-common-radius.ok", timeout=3000)
                ok_btn.click()
            except:
                pass
            time.sleep(0.25)

def update_phone_number(page, phone_number: str):
    """
    Go to account details and update phone number field.
    """
    print(f"📱 Updating phone number to: {phone_number}")
    page.goto("https://www.bullionstar.com/myaccount/details", wait_until="networkidle")

    phone_input = page.locator("input#phone-number.account-phone-number")

    # Clear existing value
    phone_input.fill("")

    # Fill with new number
    phone_input.type(phone_number)

    save_btn = page.locator("div#btn-save-changes.btn-common.tall")
    save_btn.click()
    print("✅ Phone number updated (but not saved yet)")


def main():
    numbers_manager = NumbersManager("database/bullionstar_database.db")
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            PROFILE_PATH,
            headless=False,
            args=["--start-maximized"]
        )
        page = browser.new_page()

        while True:
            number_id, number = numbers_manager.get_available_number()
            page.goto("https://www.bullionstar.com/setalerts", wait_until="networkidle")
            spot_price = get_spot_price(page)
            manage_alerts(page, spot_price)

            print(f"Cycle complete. Refreshing in {REFRESH_DELAY}s...\n")
            try:
                page.wait_for_timeout(REFRESH_DELAY * 1000)
            except KeyboardInterrupt:
                pass
            update_phone_number(page, number[3:])  # Example phone number
        browser.close()


if __name__ == "__main__":
    main()
