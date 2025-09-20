from playwright.sync_api import Playwright, sync_playwright, expect
from utiles import NumbersManager
import time
numbers_manager = NumbersManager("database/socios_database.db")
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.socios.com/onboarding")
    page.get_by_test_id("onboarding-login-button").click()
    page.set_viewport_size({"width": 1920, "height": 1080})
    while True:
        number_id, number = numbers_manager.get_available_number()
        if not number:
            print("No more numbers available.")
            break
        print("Using number:", number)
        try:
            page.get_by_test_id("login-phone-country-select-input-container").locator("span").click()
            page.get_by_test_id("login-phone-country-select-input").fill("indonesia")
            page.get_by_test_id("login-phone-country-select-item--0").get_by_test_id("list-item-container").click()
            page.get_by_test_id("login-phone-mobile-number").click()
            page.get_by_test_id("login-phone-mobile-number").fill(number[2:])
            page.get_by_test_id("login-confirm-button").click()
            page.wait_for_selector("text=Enter your Code:", timeout=60000)
        except Exception as e:
            pass
        finally:
            print("Waiting for the SMS...")
            time.sleep(5)
            numbers_manager.check_number(number_id, number)
        
        context.clear_cookies()
        page.reload()
    # ---------------------
    context.close()
    browser.close()
