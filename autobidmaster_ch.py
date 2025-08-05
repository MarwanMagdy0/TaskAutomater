from playwright.sync_api import sync_playwright
from web_automater_utiles import wait_for_selector
from utiles import NumbersManager
import os, sys, random, time
import string

def random_email():
    domains = ["gmail.com", "yahoo.com"]
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)).lower()
    random_domain = random.choice(domains)
    return f"{random_name}@{random_domain}"

numbers_manager = NumbersManager("database/autobitmaster_database.db")
proxies = [
    ["https://www.croxyproxy.rocks/", "input#url", 'button#requestSubmit'],
    ["https://proxyium.com/?__cpo=1", "input#unique-form-control", "button#unique-btn-blue"],
    # ["https://coproxy.io/free-web-proxy/", "input#hrefProxy", "input.navbtn"]
]
proxy_index = 0

while True:
    number_id, number = numbers_manager.get_available_number()
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            all_cookies = context.cookies()
            browsec_cookies = [cookie for cookie in all_cookies if "browsec.com" in cookie['domain']]
            context.clear_cookies()
            context.add_cookies(browsec_cookies)
            page = context.new_page()
            # page.goto("https://proxyium.com/?__cpo=1")  # Open any URL you want
            page.goto(proxies[proxy_index][0])  # Open any URL you want
            # page.fill('input#unique-form-control', 'https://www.autobidmaster.com/en/register-online-auto-auctions/')
            page.fill(proxies[proxy_index][1], 'https://www.autobidmaster.com/en/register-online-auto-auctions/')
            print("✅ Filled the input field")
            # Click the "Go!" button
            page.click(proxies[proxy_index][2])  
            # page.click('button#unique-btn-blue')
            print("✅ Clicked the submit button")
            page.wait_for_selector("text=+", timeout=30000)
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
            print("✅ Number is clicked")
            page.wait_for_timeout(500)
            page.type('input#phoneNumber', number[3:], delay=10)
            print("✅ Filled phone number")
            # Step 4: Fill random email
            email = random_email()
            page.fill('input#email', email)
            print(f"✅ Filled email: {email}")

            # Step 5: Click "REGISTER NOW" button
            page.click('button.qa_registration_button')
            print("✅ Clicked REGISTER NOW")
            st= time.time()
            while time.time()- st < 20:
                if wait_for_selector(page, 'text=Upgrade Your Membership Plan', timeout=100):
                    break

                if wait_for_selector(page, 'text=Invalid email address format', timeout=100):
                    print("❌ Invalid email address format. Retrying...")
                    break

                if wait_for_selector(page, 'text=Congratulations', timeout=100):
                    print("❌ Congratulations Page. Retrying...")
                    # page.wait_for_timeout(100000000)
                    break

            browser.close()
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            if 'browser' in locals():
                browser.close()
    
    proxy_index +=1
    if proxy_index == len(proxies):
        proxy_index = 0

# 01211776161