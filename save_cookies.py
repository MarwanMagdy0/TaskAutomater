from playwright.sync_api import sync_playwright
from utiles import FileManager
import json
import time

generate_cookies_file = lambda file_name : f"tradingview_cookies_25_7/{file_name}.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})

    try:
        tempmail_page = context.new_page()
        tempmail_page.set_viewport_size({"width": 1920, "height": 1080})
        tempmail_page.goto("https://temp-mail.io/en")
        tempmail_page.wait_for_selector('text="change"')
        tempmail_page.click('text="change"')
        tempmail_page.click('text="Random"')
        tempmail_page.click('//*[@id="v-0-2-1"]')
        tempmail_page.click('text="mrotzis.com"')
        tempmail_page.click('text="Get it!"')
        tempmail_page.wait_for_timeout(1000)
        email_value = ''
        while not email_value:
            email_value = tempmail_page.locator('//*[@id="email"]').input_value()
            tempmail_page.wait_for_timeout(1000)
        print("Email value:", email_value)

        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto("https://ar.tradingview.com/pricing/?source=account_activate&feature=redirect")  # 🔐 Replace with your URL
        page.get_by_role("button", name="افتح قائمة المستخدم").click()
        page.get_by_role("menuitem", name="تسجيل الدخول").click()
        page.get_by_role("link", name="Sign up").click()
        page.get_by_role("button", name="البريد الإلكتروني").click()
        page.wait_for_selector('//*[@id="id_email"]')
        page.locator('//*[@id="id_email"]').type(email_value)
        page.locator('//*[@id="id_password"]').type(email_value)
        print("🕒 Waiting for you to close the TradingView tab...")
        page.wait_for_selector('text="الرجاء تأكيد بريدك الإلكتروني"', timeout=240000)
        tempmail_page.bring_to_front()
        try:
            list_message = tempmail_page.locator("li[data-qa='message']").filter(has_text="تأكيد بريدك الإلكتروني").first
            list_message.wait_for(state="visible", timeout=240000)  # Wait up to 30 seconds
            list_message.click()
        except Exception as e:
            print("❌ Error finding confirmation message:", e)
            raise
            
        try:
            activate_link = tempmail_page.locator("a", has_text="فعِّل حسابك")
            activate_link.wait_for(state="visible", timeout=10000)
            activate_link.click()
        except Exception as e:
            print("❌ Error clicking activation link:", e)
            raise
        
        three_pages = False
        while True:
            try:
                print(page.title())
            except Exception:
                print("❌ Page closed.")
                break
            time.sleep(1)
            if len(context.pages) == 3 and not three_pages:
                three_pages = True
                latest_page = context.pages[-1]
                checkboxes = latest_page.locator("span.check-ywH2tsV_")
                checkboxes.nth(0).click()
                checkboxes.nth(1).click()

                next_button = latest_page.locator("button", has_text="التالي")
                next_button.wait_for(state="visible", timeout=10000)
                next_button.click()
    
    except KeyboardInterrupt:
        print("❌ Interrupted manually.")

    print("💾 Saving cookies...")
    state = context.storage_state()
    cookies = state.get("cookies", [])
    cookies_file = generate_cookies_file(email_value.split("@")[0])
    print(f"Cookies will be saved to: {cookies_file}")
    with open(cookies_file, "w") as f:
        json.dump(cookies, f, indent=2)
    
    file_manager = FileManager("emails.json")
    file_manager.init_key(cookies_file)
    print(f"Email {email_value} saved with cookies in {cookies_file}.")

    print("✅ Cookies saved to cookies.json")
    # input("Press Enter to close the browser...")
    browser.close()


# print list of fies in the directory
import os
directory = os.path.dirname(cookies_file)
print("Files in directory:", len(os.listdir(directory)), "files")
