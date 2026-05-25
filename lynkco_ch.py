import re
from playwright.sync_api import Playwright, sync_playwright, expect
from utiles import NumbersManager

def run(playwright: Playwright, number) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
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
    frame.get_by_text("Phone number").fill(number)
    # frame.get_by_placeholder("\n            Phone number\n          ").fill(number)
    frame.get_by_placeholder("Email").click()
    frame.get_by_placeholder("Email").fill("marwan1779724366@wshu.net")
    frame.get_by_placeholder("Password").click()
    frame.get_by_placeholder("Password").fill("au9wueykiz@osxofulk.com")
    frame.get_by_text("I confirm that I am 18 years").click()
    frame.get_by_text("Yes, please send me regular").click()
    
    btn = frame.get_by_label("Continue")
    expect(btn).to_be_enabled(timeout=150000)
    btn.click()

    # page.get_by_role("main").locator("iframe[title=\"Create account \"]").content_frame.get_by_placeholder("\n            Verification Code\n          ").fill(code)
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
