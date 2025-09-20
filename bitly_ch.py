from playwright.sync_api import sync_playwright
from utiles import time_logg, EmailManager, NumbersManager
from web_automater_utiles import wait_for_selector
from bitly_country_codes import CODE_TO_COUNTRY
import json, time

numbers_manager = NumbersManager("database/bitly_database.db")
print(numbers_manager.get_country_codes())
email_manager = EmailManager("database/bitly_database.db")
while True:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--disable-web-security", "--disable-features=IsolateOrigins,site-per-process"])


        context = browser.new_context()
        all_cookies = context.cookies()
        browsec_cookies = [cookie for cookie in all_cookies if "browsec.com" in cookie['domain']]
        context.clear_cookies()
        context.add_cookies(browsec_cookies)
        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto("https://tempmail.so/")  # Open any URL you want
        page.wait_for_timeout(1500)

        page.wait_for_selector('span.text-base.truncate')

        # Get the text content
        email = page.locator('span.text-base.truncate').inner_text()
        print("Extracted email:", email)
        bitly = context.new_page()
        # bitly.set_viewport_size({"width": 1920, "height": 1080})
        bitly.goto("https://app.bitly.com/settings/profile")
        bitly.get_by_role("link", name="Sign up").click()
        bitly.wait_for_selector('input[type="email"]')
        bitly.locator('input[type="email"]').fill(email)
        bitly.locator('input[type="password"]').fill("Wm8$zLp2!xR#Qb17Tf")
        # click button id accept-recommended-btn-handler
        bitly.locator("button#onetrust-accept-btn-handler").click(timeout=60000)
        bitly.locator("button:has-text('Create')").click()
        page.bring_to_front()
        page.wait_for_timeout(4000)
        try:
            print("Waiting the Dialog...")
            page.get_by_role("button", name="Close").click(timeout=60000)
        except Exception as e:
            print("❌ Error Waiting the Dialog:", e)

        page.get_by_text("Bitly validation code", exact=True).click(timeout=60000)
        code = page.locator("p[style*='color:#ee6123']").text_content().strip()
        print("Bitly code:", code)
        bitly.bring_to_front()
        bitly.locator("input[type='text'][maxlength='6']").fill(code)  # replace with your actual code

        bitly.locator("button[type='submit'].css-8m0ph1").click()
        bitly.locator("button.orb-button.default", has_text="Continue").click(timeout=6000000)
        bitly.locator("button.orb-button.default", has_text="Continue").click(timeout=6000000)
        bitly.locator("button", has_text="I'll jump in on my own").click()
        bitly.click('div.menu-item:has-text("Settings")', timeout=60000)
        cookies = context.cookies()
        print("💾 Saving cookies...")
        state = context.storage_state()
        cookies = state.get("cookies", [])
        
        email_manager.insert_email_with_cookies(email.split("@")[0], json.dumps(cookies))
        print("Cookies are Saved!")
        for countru_code in numbers_manager.get_country_codes():
            print(countru_code, CODE_TO_COUNTRY.get(countru_code, "Unknown"))
            number_id, number = numbers_manager.get_available_number(countru_code)
            if not number:
                print("No available numbers. Exiting...")
                break
            country_code, national_number = numbers_manager.split_number(number)
            bitly.select_option("#two-factor-country-code", label=CODE_TO_COUNTRY[country_code]) # Senegal (+221)
            bitly.locator('#profile-mobile-number').clear()
            bitly.fill('#profile-mobile-number', national_number)  # Replace with desired number
            # Click the send button
            bitly.click("button:has-text('Send verification code')", timeout=60000)
            time_logg("Send verification code")
            while True:
                if wait_for_selector(bitly, "text=verification code has been sent", timeout=100):
                    print("[Done]")
                    bitly.wait_for_timeout(3000)
                    numbers_manager.check_number(number_id, number)
                    email_manager.log_status(email, "CODE_SENT")
                    break
                elif wait_for_selector(bitly, "text=Failed to set phone number", timeout=100):
                    print("[Failed]")
                    email_manager.log_status(email, "Failed")
                    break
            page.wait_for_timeout(5 * 1000)
            page.reload(wait_until="networkidle")
            page.wait_for_timeout(5 * 1000)

        
        browser.close()
    # A verification code has been sent to your phone
    # Failed to set phone number
    time.sleep(60 * 6)
