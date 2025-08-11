import re
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-infobars",
        ]
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        locale="en-US",
        viewport={"width": 1280, "height": 800}
    )

    # Inject JS to remove navigator.webdriver
    context.add_init_script(
        """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        window.navigator.chrome = {
            runtime: {},
        };
        Object.defineProperty(navigator, 'languages', {
            get: () => ['en-US', 'en']
        });
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5],
        });
        """
    )

    page = context.new_page()
    page.goto("https://www.cathaypacific.com/cx/fr_FR/membership/sign-up.html", timeout=60000)
    page.wait_for_timeout(timeout=2000000)

    # Wait for iframe to load
    frame = page.frame_locator('iframe')
    account_input = frame.locator('input[placeholder="Please set the account name"]')
    account_input.wait_for(timeout=20000)

    # Fill the registration form
    account_input.fill("anaesmymarwan")
    frame.get_by_text("Egypt+20Search").click()
    frame.get_by_placeholder("Search").fill("60")
    frame.get_by_text("Malaysia").click()
    frame.get_by_placeholder("Enter the mobile number").fill("1156502516")
    frame.get_by_placeholder("Set the login password").fill("147852Y#")
    frame.get_by_placeholder("Enter the login password again").fill("147852Y#")
    frame.get_by_label("I have carefully read,").check()
    frame.get_by_role("button", name="Agree and Register").click()


    print("Slider captcha appeared. Solve it manually...")
    input("Press Enter after solving the slider captcha...")

    # Close everything
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
