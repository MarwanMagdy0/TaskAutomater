import re
from playwright.sync_api import Playwright, sync_playwright, expect
from utiles import NumbersManager

def run(playwright: Playwright, number) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    tempmail_page = context.new_page()
    tempmail_page.set_viewport_size({"width": 1920, "height": 1080})
    tempmail_page.goto("https://temp-mail.io/en")
    email_value = ''
    while not email_value:
        email_value = tempmail_page.locator('//*[@id="email"]').input_value()
        tempmail_page.wait_for_timeout(1000)
    print("Email value:", email_value)
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://www.lynkco.com/en/create-account")
    page.get_by_role("button", name="Accept all cookies").click()
    frame = page.get_by_role("main").locator("iframe[title=\"Create account \"]").content_frame
    frame.locator("#otherCountries").select_option("SI")
    frame.get_by_placeholder("First name").click()
    frame.get_by_placeholder("First name").fill("asdasdasd")
    frame.get_by_text("Last name").click()
    frame.get_by_placeholder("Last name").fill("qweqweqweqwe")
    frame.get_by_text("Phone number").click()
    frame.get_by_placeholder("\n            Phone number\n          ").fill(number)
    frame.get_by_placeholder("Email").click()
    frame.get_by_placeholder("Email").fill(email_value)
    frame.get_by_placeholder("Password").click()
    frame.get_by_placeholder("Password").fill("au9wueykiz@osxofulk.com")
    frame.get_by_text("I confirm that I am 18 years").click()
    frame.get_by_text("Yes, please send me regular").click()
    btn = frame.get_by_label("Continue")
    expect(btn).to_be_enabled(timeout=150000)
    btn.click()
    frame.get_by_text("Verification Code", exact=True).click()
    try:
        list_message = tempmail_page.locator("li[data-qa='message']").filter(has_text="Verify your Lynk & Co account.").first
        list_message.wait_for(state="visible", timeout=240000)  # Wait up to 30 seconds
        list_message.click()

        code = tempmail_page.locator("span[style*='color:#0DCEA7']").text_content().strip()
        print("Lynkco code:", code)

    except Exception as e:
        print("❌ Error finding confirmation message:", e)
        raise
    page.get_by_role("main").locator("iframe[title=\"Create account \"]").content_frame.get_by_placeholder("\n            Verification Code\n          ").fill(code)
    page.wait_for_timeout(10000)
    # ---------------------
    context.close()
    browser.close()

numbers_manager = NumbersManager("database/lynk_database.db")

while True:
    number_id, number = numbers_manager.get_available_number()
    try:
        with sync_playwright() as playwright:
            run(playwright, number[3:])
            numbers_manager.check_number(number_id, number)
    except Exception as e:
        print(f"Error : {e}")
