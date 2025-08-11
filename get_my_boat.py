from playwright.sync_api import Playwright, sync_playwright, expect
from web_automater_utiles import wait_for_selector
from faker import Faker
import re, time, random


faker = Faker()
data = {}
data["MZ"] = [
    "258829030270",
    "258827261079",
    "258825898193",
    "258824966964",
    "258824183541",
    "258823296942",
    "258823183025",
    "258821449152",
    "258820947531",
    "258820815682",
    "258820722701",
    "258820422526",
    "258820095329",
    "258820086768"
]

data["MY"] = [
    "601159732248",
    "601157846976",
    "601157528349",
    "601156966369",
    "601156911482",
    "601113231577",
    "601113193424",
    "60103351727",
]
proxies = [
    ["https://www.croxyproxy.rocks/", "input#url", 'button#requestSubmit'],
    ["https://proxyium.com/?__cpo=1", "input#unique-form-control", "button#unique-btn-blue"],
    ["https://proxypal.net/", 'input[name="url"]', "button.check-button"],
]

def run(playwright: Playwright, country, number) -> None:
    proxy_index = random.randint(0, 2)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    all_cookies = context.cookies()
    browsec_cookies = [cookie for cookie in all_cookies if "browsec.com" in cookie['domain']]
    context.clear_cookies()
    context.add_cookies(browsec_cookies)
    page = context.new_page()
    # page.set_viewport_size({"width": 1500, "height": 1200})
    page.goto(proxies[proxy_index][0])  # Open any URL you want
    page.fill(proxies[proxy_index][1], 'https://www.getmyboat.com')
    print("✅ Filled the input field")
    # Click the "Go!" button
    page.click(proxies[proxy_index][2])  

    page.set_default_timeout(20000)

    page.get_by_role("button", name="Close").click(timeout=60000)
    # page.evaluate("document.body.style.zoom=0.8")
    # page.evaluate("document.body.style.zoom=0.25")
    page.locator("[data-test=\"MainMenuDropDown\"]").get_by_label("Main menu").click(timeout=60000)
    # page.evaluate("document.body.style.zoom=0.25")
    page.get_by_role("link", name="Create Account").click(timeout=60000)
    page.get_by_placeholder("First name").fill(faker.user_name())
    page.get_by_placeholder("Last name").fill(faker.last_name())
    page.get_by_placeholder("Your email").fill(faker.email())
    page.get_by_label("Phone number country").select_option(country)
    # time.sleep(100)
    page.get_by_placeholder("Phone number").fill(number)
    page.get_by_placeholder("Password", exact=True).fill("asuidyuiqw@sahdj%^$%^8978")
    page.get_by_placeholder("Re-enter password").fill("asuidyuiqw@sahdj%^$%^8978")
    page.get_by_text("Yes").click(timeout=60000)
    page.get_by_role("button", name="Create Account").click(timeout=60000)
    page.get_by_role("button", name="Accept").click(timeout=60000)
    # page.evaluate("document.body.style.zoom=0.25")
    if wait_for_selector(page, "text=reCAPTCHA", 10000):
        page.get_by_text("Yes").click()
        page.get_by_role("button", name="Create Account").click(timeout=60000)
        page.get_by_role("button", name="Accept").click(timeout=60000)

    print("[PASSED]")
    page.locator("[data-test=\"MainMenuDropDown\"]").get_by_label("Main menu").click(timeout=60000)
    page.get_by_role("button", name="Account").click(timeout=60000)
    page.get_by_role("button", name="Verify phone number").click(timeout=60000)
    page.get_by_label("Enter verification code").locator("[data-test=\"close-button\"]").click(timeout=60000)
    # new_nums = ["+601156758991", "+60103022959", "+60103351727"]
    # for i in range(3):
    #     page.get_by_role("button", name="Change phone number").click()
    #     page.get_by_label("Enter password*").click()
    #     page.get_by_label("Enter password*").fill("asuidyuiqw@sahdj%^$%^8978")
    #     page.get_by_placeholder("Enter your phone number").click()
    #     page.keyboard.press("Control+A")
    #     page.keyboard.press("Delete")
    #     page.get_by_placeholder("Enter your phone number").fill(new_nums[i])
    #     page.get_by_role("button", name="Confirm Phone Number").click()
    #     page.get_by_label("Enter verification code").locator("[data-test=\"close-button\"]").click()
        # time.sleep(2)
    # ---------------------
    context.close()
    browser.close()
    return True

with sync_playwright() as playwright:
    for country, numbers in data.items():
        print(country)
        if country in ["SN", "MZ", "UZ"]:
            continue
        for number in numbers:
            print(number)
            try:
                print(run(playwright, country, number))
            except Exception as e:
                print(f"❌ Error occurred: {e}")
