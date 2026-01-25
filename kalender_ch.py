import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://business.bokadirekt.se/sign-up-complete")
    page.get_by_label("Acceptera alla").click()
    page.get_by_role("link", name="Prova gratis").click()
    page.get_by_placeholder("Förnamn Efternamn").click()
    page.get_by_placeholder("Förnamn Efternamn").fill("Docusign")
    page1 = context.new_page()
    page1.goto("https://priyo.email/")
    page1.get_by_label("Copy to clipboard").nth(1).click()
    page.get_by_placeholder("adress@exempel.se").click()
    time.sleep(10)
    page.get_by_placeholder("0701234567").click()
    page.get_by_placeholder("0701234567").fill("0701234567")
    page.get_by_role("button", name="Fortsätt").click()
    page.get_by_placeholder("Fyll i företagets namn").click()
    page.get_by_placeholder("Fyll i företagets namn").fill("Docusign")
    page.get_by_placeholder("Sök efter din address").click()
    page.get_by_placeholder("Sök efter din address").fill("st")
    page.get_by_text("StockholmSweden").click()
    page.get_by_role("button", name="Fortsätt skapa konto").click()
    page1.locator("div").filter(has_text=re.compile(r"^Välj lösenord till Bokadirekt$")).click()
    with page1.expect_popup() as page2_info:
        page1.locator("#message-6897807 iframe").content_frame.get_by_role("link", name="Välj lösenord").click()
    page2 = page2_info.value
    page2.get_by_label("Lösenord", exact=True).click()
    page2.get_by_label("Lösenord", exact=True).fill("noreply@transactional.bokadirekt.se")
    page2.get_by_label("Lösenord upprepat").click()
    page2.get_by_label("Lösenord upprepat").fill("noreply@transactional.bokadirekt.se")
    page2.get_by_role("button", name="Välj lösenord").click()
    page2.goto("https://portal.bokadirekt.se/client/welcome-dialog")
    page2.get_by_role("button", name="Kom igång").click()
    page2.locator("div").filter(has_text=re.compile(r"^MiniFrån279kr/månadVälj$")).get_by_role("button").click()
    page2.get_by_role("button", name="Välj abonnemang").click()
    page2.locator("m3-input div").filter(has_text="Organisationsnummer:").nth(4).click()
    page2.locator("m3-input").get_by_role("button").click()
    page2.get_by_role("textbox").fill("212000-5513")
    page2.locator("iframe[name=\"intercom-notification-stack-frame\"]").content_frame.get_by_test_id("notification-close-desktop").click()
    page2.get_by_role("button", name="Fortsätt").click()
    page2.get_by_role("button", name="Välj abonnemang").click()
    page2.locator("m3-edit-dialog-header-close").get_by_role("button").click()
    page2.get_by_role("button", name="Gå till onlinebokning").click()
    page2.get_by_label("Logga ut").click()
    page2.locator("m3-edit-dialog-header-close").get_by_role("button").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
