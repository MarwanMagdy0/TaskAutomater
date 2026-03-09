from playwright.sync_api import sync_playwright
from utiles import time_logg, EmailManager, NumbersManager
from web_automater_utiles import wait_for_selector
from bitly_country_codes import CODE_TO_COUNTRY
import json, time
from tqdm import tqdm

numbers_manager = NumbersManager("database/bitly_database.db")
print(numbers_manager.get_country_codes())
email_manager = EmailManager("database/bitly_database.db")
sleep_time = 5  # Minutes
total_seconds = int(60 * sleep_time)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-web-security", "--disable-features=IsolateOrigins,site-per-process"])
    context = browser.new_context()
    all_cookies = context.cookies()
    browsec_cookies = [cookie for cookie in all_cookies if "browsec.com" in cookie['domain']]
    context.clear_cookies()
    context.add_cookies(browsec_cookies)
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://boomlify.com/")
    page.wait_for_timeout(1500)

    page.locator("xpath=/html/body/div[1]/div[2]/div/main/div[1]/div/div/div/div[1]/div[2]/div/button").click()
    page.get_by_label("View inbox for").click()
    time.sleep(5)
    email = page.locator("h1.text-base").inner_text()
    print("Extracted email:", email)

    bitly = context.new_page()
    bitly.set_viewport_size({"width": 1920, "height": 1080})
    bitly.goto("https://bitly.com/a/sign_up")
    bitly.get_by_role("button", name="Accept All").click()
    bitly.get_by_label("Email").fill(email)
    bitly.get_by_label("Password", exact=True).fill("og!yQ6(w5%2_")
    bitly.get_by_role("button", name="Create free account").click()
    time.sleep(5)

    page.get_by_role("button", name="Refresh emails").click()
    page.get_by_text("NondonJust nowBitly").click()
    code = page.locator("p[style*='color:#ee6123']").inner_text().strip()
    print("Bitly code:", code)

    bitly.get_by_label("Enter code").fill(code)
    bitly.get_by_role("button", name="Verify").click()
    bitly.get_by_role("button", name="Remind me later").click()
    bitly.locator("[data-test-id=\"settings\"]").click()

    # Phone verification part
    for country_code in ["221", "222", "244", "258", "992", "368"]:
        print("using:", country_code)
        number_id, number = numbers_manager.get_available_number(country_code)
        if not number:
            print("No available numbers. Exiting...")
            break
        _, national_number = numbers_manager.split_number(number)
        if national_number is None:
            continue
        bitly.select_option("#two-factor-country-code", label=CODE_TO_COUNTRY[country_code])  # Senegal (+221)
        bitly.locator('#profile-mobile-number').clear()
        bitly.fill('#profile-mobile-number', national_number)
        bitly.click("button:has-text('Send verification code')", timeout=60000)
        time_logg("Send verification code")
        while True:
            if wait_for_selector(bitly, "text=verification code has been sent", timeout=100):
                print("[Done]")
                bitly.wait_for_timeout(3000)
                numbers_manager.check_number(number_id, number, False)
                # email_manager.log_status(email, "CODE_SENT")
                break
            elif wait_for_selector(bitly, "text=Failed to set phone number", timeout=100):
                print("[Failed]")
                # email_manager.log_status(email, "Failed")
                break
        
        bitly.reload()
        time.sleep(5)

    # Save cookies
    cookies = context.cookies()
    print("💾 Saving cookies...")
    state = context.storage_state()
    cookies = state.get("cookies", [])
    email_manager.insert_email_with_cookies(email.split("@")[0], json.dumps(cookies))
    print("Cookies are Saved!")

    browser.close()
