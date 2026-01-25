import re, time
from playwright.sync_api import Playwright, sync_playwright, expect
from web_automater_utiles import safe_load
import random
import requests
itt = None
def handle_response(response):
    global itt
    url = response.url
    try:
        if "itt" in url:
            itt = url.split("/intents/")[1].split("/")[0]
            print(f"Extracted ITT: {itt}")
    except Exception as e:
        print(f"Error extracting ITT from URL {url}: {e}")

numbers = ['60121229', '60105895', '61502066', '65535718', '70882639', '60781816', 
 '79204552', '60121296', '60738355', '79061763', '79858158', '70088791', 
 '70749141', '60987071', '65646739', '70395238', '65920492', '70119410', 
 '79921360', '60739255', '79037469', '60350379', '60878208', '60196293', 
 '79401216']



def run(playwright: Playwright) -> None:
    global itt
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    print("Browser and context initialized.")
    
    page.on("response", handle_response)
    safe_load(page, "https://maridalsveiensmadyrklinikk.youcanbook.me/")
    print("Navigated to the website.")
    
    page.get_by_test_id("cookie_consent_accept").click()
    print("Accepted cookie consent.")
    
    page.get_by_test_id("at_jsid8884817").click()
    print("Clicked on the specified element with test ID 'at_jsid8884817'.")
    
    for _ in range(0, random.randint(5, 15)):
        page.click('button[aria-label="Next Month"]')

    
    page.locator('button[aria-disabled="false"]').first.click()
    print("Clicked on the first available button.")
    
    page.locator('._slot_column_1dulf_11').first.click()
    print("Clicked on the first slot column.")
    
    page.get_by_test_id("Q2").click()
    print("Clicked on the input field with test ID 'Q2'.")
    
    page.get_by_test_id("Q2").fill("tmama")
    print("Filled 'tmama' in the input field with test ID 'Q2'.")
    
    page.get_by_role("button", name="Egypt: +").click()
    print("Clicked on the button with name 'Egypt: +'.")
    
    page.get_by_role("option", name="Bolivia +").click()
    print("Selected the option 'Bolivia +' from the dropdown.")
    
    random_number = random.choice(numbers)
    page.get_by_test_id("Q3").fill(f"{random_number}")
    print(f"Filled '{random_number}' in the input field with test ID 'Q3'.")
    
    page.get_by_test_id("Q3").click()
    print("Clicked on the input field with test ID 'Q3'.")
    
    page.get_by_test_id("EMAIL").click()
    print("Clicked on the input field with test ID 'EMAIL'.")
    
    page.get_by_test_id("EMAIL").fill("czb6fcp@tempblockchain.com")
    print("Filled 'czb6fcp@tempblockchain.com' in the input field with test ID 'EMAIL'.")
    
    page.get_by_test_id("confirm_button").click()
    print("Clicked on the confirm button.")
    
    time.sleep(15)
    print(itt)
    print("Waited for 7 seconds.")
    print("Successfully made the request to cancel the booking.")
    new_page = page.context.new_page()
    new_page.goto(f"https://book.youcanbook.me/?i={itt}&ro=b&o=c")
    new_page.click('button:has-text("Confirm Cancellation")')
    print("Clicked on 'Confirm Cancel'.")
    time.sleep(5)
    context.close()
    print("Context closed.")
    
    browser.close()
    print("Browser closed.")

while True:
    try:
        with sync_playwright() as playwright:
            run(playwright)
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1)