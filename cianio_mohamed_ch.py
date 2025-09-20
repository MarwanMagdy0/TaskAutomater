import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mozi-login.alibaba-inc.com/mozi/smsRegister.htm?registerNamespace=zhaopin")
    page.get_by_role("textbox", name="Please enter your cell phone").click()
    page.get_by_role("textbox", name="Please enter your cell phone").fill("1156548617")
    page.locator(".intl-tel-arrow").first.click()
    page.get_by_text("Support characters search").first.click()
    page.get_by_placeholder("Click search").fill("mala")
    page.get_by_text("Malaysia60").first.click()
    # Wait for the textbox to have exactly 4 characters
    page.get_by_role("textbox", name="Please enter the image code").click()
    while len(page.get_by_role("textbox", name="Please enter the image code").input_value()) != 4:
        page.wait_for_timeout(100)  # Wait for 100ms before checking again
        print(page.get_by_role("textbox", name="Please enter the image code").text_content())
    page.get_by_role("button", name="Send SMS").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
