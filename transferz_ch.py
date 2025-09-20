from playwright.sync_api import Playwright, sync_playwright, expect
from utiles import NumbersManager
import time
numbers_manager = NumbersManager("database/transferz_database.db")
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://transferz.taxi/phone")
    page.set_viewport_size({"width": 1920, "height": 1080})
    while True:
        number_id, number = numbers_manager.get_available_number()
        if not number:
            print("No more numbers available.")
            break
        print("Using number:", number)
        try:
            page.get_by_test_id("dropdown_country-code").click()
            time.sleep(1)
            page.locator("#react-select-3-input").fill("62")
            time.sleep(1)
            page.get_by_text("Indonesia +").click()
            time.sleep(1)
            page.get_by_test_id("input_phone-number").click()
            time.sleep(1)
            page.get_by_test_id("input_phone-number").fill(number[2:])
            time.sleep(1)
            page.get_by_test_id("custom-button").click()
            time.sleep(1)
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
