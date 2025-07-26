from playwright.sync_api import sync_playwright
from utiles import PhoneStatusManager, EmailManager, time_logg
from web_automater_utiles import wait_for_selector
from ims_client import IMSClient
import time



phone_manager = PhoneStatusManager("numbers.json")
email_manager = EmailManager("emails.json")
ims_client = IMSClient()

with sync_playwright() as p:
    number = phone_manager.get_next_number_status()
    email = email_manager.get_email()
    email_manager.email_is_used(email)
    if email is None:
        time_logg("No available email found.")
        exit(1)
    print(f"Using number: {number}, email: {email}")
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://ar.tradingview.com/settings/#account-settings")
    try:
        page.wait_for_selector('//*[@id="tv-content"]/div/div/div/div/div/div[3]/button', timeout=240000)
        page.click('//*[@id="tv-content"]/div/div/div/div/div/div[3]/button')
        page.wait_for_selector("text=البريد الإلكتروني", timeout=240000)
        page.click("text=البريد الإلكتروني")
        page.wait_for_selector('//*[@id="id_username"]', timeout=240000)
        page.fill('//*[@id="id_username"]', email)
        page.fill('//*[@id="id_password"]', email)
        try:
            page.click('xpath=/html/body/div[7]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button', timeout=1000)
            page.click('xpath=/html/body/div[8]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button', timeout=1000)
        except:
            pass
        print('clicking "Add phone"')

        
        page.wait_for_selector("text=Add phone", timeout=240000)
        page.click("text=Add phone")
        try:
            page.wait_for_selector("#\:rg\: > span.inner-slot-W53jtLjw.interactive-W53jtLjw > span", timeout=5000)
            page.click("#\:rg\: > span.inner-slot-W53jtLjw.interactive-W53jtLjw > span")
        except:
            print("No phone number slot found, continuing...")

        page.wait_for_selector("text=موزانبيق", timeout=240000)
        page.click("text=موزانبيق")
        try:
            page.fill('//*[@id=":rf:"]', f"{number}"[3:], timeout=5000)
        except:
            print("Enter the number manually in the input field.")
        time.sleep(2)
        page.click("text=احصل على الرمز")
        # wait for Verify your phone number
        if wait_for_selector(page, "text=Verify your phone number", timeout=240000):
            for _ in range(3):
                page.wait_for_selector("text=أعد إرسال رسالة", timeout=240000) # 4 minuits
                page.click("text=أعد إرسال رسالة")
                time.sleep(4)
                email_manager.increment_email_usage(email)
                # Check if the number exists in IMS logs
                if ims_client.number_exists(number):
                    email_manager.email_is_used(email)
                    time_logg(f"Number {number} exists in IMS logs.")
                    phone_manager.update_number_status(number, is_working=True)
                else:
                    time_logg(f"Number {number} does not exist in IMS logs.")
                    phone_manager.update_number_status(number, is_working=False)
                    email_manager.restore_email(email)
                    break
        
        email_manager.email_is_used(email)
        time.sleep(12000)
    
    except Exception as e:
        time_logg(f"An error occurred: {e}")
