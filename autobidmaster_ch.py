from playwright.sync_api import sync_playwright
from web_automater_utiles import wait_for_selector
import os, sys, random
import string

def random_email():
    domains = ["example.com", "testmail.com", "mymail.com"]
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    random_domain = random.choice(domains)
    return f"{random_name}@{random_domain}"

while True:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            all_cookies = context.cookies()
            browsec_cookies = [cookie for cookie in all_cookies if "browsec.com" in cookie['domain']]
            context.clear_cookies()
            context.add_cookies(browsec_cookies)
            page = context.new_page()
            page.goto("https://proxyium.com/?__cpo=1")  # Open any URL you want
            page.fill('input#unique-form-control', 'https://www.autobidmaster.com/en/register-online-auto-auctions/')
            # page.fill('input#url', 'https://www.autobidmaster.com/en/register-online-auto-auctions/')
            print("✅ Filled the input field")
            # Click the "Go!" button
            # page.click('button#requestSubmit')
            page.click('button#unique-btn-blue')
            print("✅ Clicked the submit button")
            page.wait_for_selector("text=+", timeout=150000)
            print("✅ Page loaded successfully")
            # Step 1: Fill First Name and Last Name
            page.fill('input#register-first-name', 'John')
            page.fill('input#register-last-name', 'Doe')
            print("✅ Filled first and last name")

            # Step 2: Click on the country flag dropdown
            page.click('div.iti__selected-flag')
            print("✅ Clicked country selector")

            # Step 3: Select Mozambique (+258) from the dropdown
            page.click('li#iti-0__item-gt')
            print("✅ Selected Mozambique (+502)")
            page.wait_for_timeout(500)
            page.type('input#phoneNumber', '58194906', delay=10)
            print("✅ Filled phone number")
            # Step 4: Fill random email
            email = random_email()
            page.fill('input#email', email)
            print(f"✅ Filled email: {email}")

            # Step 5: Click "REGISTER NOW" button
            page.click('button.qa_registration_button')
            print("✅ Clicked REGISTER NOW")
            while True:
                if wait_for_selector(page, 'text=Upgrade Your Membership Plan', timeout=100):
                    break

                if wait_for_selector(page, 'text=Invalid email address format', timeout=100):
                    print("❌ Invalid email address format. Retrying...")
                    break

                if wait_for_selector(page, 'text=Congratulations', timeout=100):
                    print("❌ Congratulations Page. Retrying...")
                    break

            browser.close()
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            if 'browser' in locals():
                browser.close()