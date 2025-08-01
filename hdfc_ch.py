# https://osappsext.hdfc.com/spotoffer_fe/BasicInformation
from playwright.sync_api import sync_playwright
import os, sys
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    all_cookies = context.cookies()
    browsec_cookies = [cookie for cookie in all_cookies if "browsec.com" in cookie['domain']]
    context.clear_cookies()
    context.add_cookies(browsec_cookies)
    tempmail_page = context.new_page()
    tempmail_page.goto("https://temp-mail.io/en")
    # tempmail_page.wait_for_selector('text="change"')
    # tempmail_page.click('text="change"')
    # tempmail_page.click('text="Random"')
    # tempmail_page.click('//*[@id="v-0-2-1"]')
    # tempmail_page.click('text="mrotzis.com"')
    # tempmail_page.click('text="Get it!"')
    tempmail_page.wait_for_timeout(1000)
    email_value = ''
    while not email_value:
        email_value = tempmail_page.locator('//*[@id="email"]').input_value()
        tempmail_page.wait_for_timeout(1000)
    print("Email value:", email_value)

    page = context.new_page()
    page.goto("https://osappsext.hdfc.com/spotoffer_fe/BasicInformation")
    locator = page.locator("button", has_text="Non-Resident Indian")
    locator.click()
    page.locator("#b6-EmailAddress").fill(email_value)
    page.wait_for_timeout(500)
    page.locator("text=Verify email").click()
    page.wait_for_timeout(1500000)