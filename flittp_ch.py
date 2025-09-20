import re, time, os
from playwright.sync_api import Playwright, sync_playwright, expect
from utiles import NumbersManager
numbers_manager = NumbersManager("database/flittp_database.db")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    while True:
        number_id, number = numbers_manager.get_available_number()
        if not number:
            print("No more numbers available.")
            break
        print("Using number:", number)
        try:
            page.goto("https://ftittp.mha.gov.in/fti/signUp", timeout=60000)
            page.set_viewport_size({"width": 1920, "height": 1080})
            page.get_by_role("textbox", name="ISD code").click()
            page.get_by_label("Search").click()
            page.get_by_label("Search").fill("258")
            page.get_by_role("option", name="+258 - MOZAMBIQUE").click()
            page.get_by_placeholder("Please enter mobile number").click()
            page.get_by_placeholder("Please enter mobile number").fill(number[3:])
            page.get_by_placeholder("Enter Code").click()
            time.sleep(2)  # Wait for 2 seconds to ensure the input is processed
            os.system("play -nq -t alsa synth 0.1 sine 1000")
            while True:
                input_box = page.get_by_placeholder("Enter Code")
                id_value = input_box.input_value()
                if len(id_value) == 6:
                    break
                time.sleep(0.5)  # Poll every 0.5 seconds
            page.get_by_role("button", name="Send OTP").click()
            # page.goto("https://ftittp.mha.gov.in/fti/sendMobileOtp")
        except Exception as e:
            print("An error occurred:", e)
        finally:
                print("Waiting for the SMS...")
                st = time.time()
                while time.time() - st < 35:  # Wait up to 35 seconds
                    if "Verify your mobile number" in page.content():
                        break
                    time.sleep(1)  # Poll every 1 second
                
                # time.sleep(30)
                # numbers_manager.check_number(number_id, number)
        context.clear_cookies()
        page.reload()

    # ---------------------
    context.close()
    browser.close()