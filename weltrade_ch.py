from playwright.sync_api import sync_playwright
from utiles import EmailManager
import json, sqlite3
import time, re
from web_automater_utiles import safe_load


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})

    try:
        tempmail_page = context.new_page()
        tempmail_page.set_viewport_size({"width": 1920, "height": 1080})
        safe_load(tempmail_page, "https://temp-mail.io/en")
        tempmail_page.wait_for_selector('text="change"')
        tempmail_page.click('text="change"')
        tempmail_page.click('text="Random"')
        tempmail_page.click('//*[@id="v-0-2-1"]')
        tempmail_page.click('text="wnbaldwy.com"')
        tempmail_page.click('text="Get it!"')
        tempmail_page.wait_for_timeout(1000)
        email_value = ''
        while not email_value:
            email_value = tempmail_page.locator('//*[@id="email"]').input_value()
            tempmail_page.wait_for_timeout(1000)
        print("Email value:", email_value)

        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        safe_load(page, "https://secure.weltrade.com/login/registration")
        page.get_by_label("Email").click()
        page.get_by_label("Email").fill(email_value)
        page.get_by_text("Password").click()
        page.get_by_label("Password").fill(email_value)
        page.locator("div").filter(has_text=re.compile(r"^Egypt$")).first.click()
        page.get_by_placeholder("Search").fill("za")
        page.get_by_text("Zambia").click()
        page.get_by_role("button", name="Create account").click()
        page.wait_for_selector('text="Confirm your email"', timeout=240000)
        tempmail_page.bring_to_front()
        try:
            list_message = tempmail_page.locator("li[data-qa='message']").filter(has_text="Confirm your email address").first
            list_message.wait_for(state="visible", timeout=240000)  # Wait up to 30 seconds
            list_message.click()
        except Exception as e:
            print("❌ Error finding confirmation message:", e)
            raise
            
        try:
            activate_link = tempmail_page.locator("a", has_text="Confirm")
            activate_link.wait_for(state="visible", timeout=10000)
            activate_link.click()
        except Exception as e:
            print("❌ Error clicking activation link:", e)
            raise
        
        time.sleep(8)
        confirmation_page = context.new_page()
        safe_load(confirmation_page, "https://secure.weltrade.com/settings/personal-data")
        confirmation_page.get_by_role("textbox", name="5123456").click(timeout=240000)
        confirmation_page.get_by_role("textbox", name="5123456").type("952156949", delay=100, timeout=24000)
        confirmation_page.get_by_role("textbox", name="5123456").fill("")
        confirmation_page.get_by_role("textbox", name="5123456").fill("952156949")
        confirmation_page.get_by_role("button", name="Continue").click(timeout=24000)
        confirmation_page.locator("a").filter(has_text="Confirm your phone number").click(timeout=24000)
        confirmation_page.get_by_role("button", name="Continue").click(timeout=24000)
        confirmation_page.get_by_role("button", name="Resend SMS").click(timeout=24000)
        # time.sleep(20)

    
    except KeyboardInterrupt:
        print("❌ Interrupted manually.")

    print("💾 Saving cookies...")
    state = context.storage_state()
    cookies = state.get("cookies", [])
    
    email_manager = EmailManager("database/weltrade_database.db")
    email_manager.insert_email_with_cookies(email_value, json.dumps(cookies))
    # https://secure.weltrade.com/settings/personal-data
    browser.close()

conn = sqlite3.connect('database/weltrade_database.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM emails WHERE DATE(datetime) = DATE('now', 'localtime');")
print("Emails saved today:", cursor.fetchone()[0])