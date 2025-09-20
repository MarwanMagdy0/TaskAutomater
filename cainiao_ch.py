import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from utiles import NumbersManager
import shutil, time, re
URL = "https://cnlogin.cainiao.com/login?isNewLogin="

def wait_until_timeout_or_closed(driver, duration=60):
    start = time.time()
    while time.time() - start < duration:
        try:
            # Try a lightweight call to check if browser is alive
            _ = driver.title
        except:
            print("🛑 Browser closed by user")
            return False  # closed early
        time.sleep(1)  # small pause to avoid 100% CPU
    print("⏰ 1 minute finished")
    return True  # lasted full duration

chrome_path = shutil.which("google-chrome") or shutil.which("chromium-browser") or "google-chrome"
numbers_manager = NumbersManager("database/cianiao_database.db")

while True:
    number_id, number = numbers_manager.get_available_number()
    # if number[-2] != "9":
    #     continue
    print(f"[{number_id}]:{number}")
    opts = uc.ChromeOptions()
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--start-maximized")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(
        options=opts,
        version_main=138,
        browser_executable_path=chrome_path
    )
    wait = WebDriverWait(driver, 20)

    try:
        driver.get(URL)
        print("🌍 Opened signup page")

        # 1) Click "SMS Login"
        sms_login_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'SMS Login')]"))
        )
        sms_login_tab.click()
        print("✅ Clicked SMS Login")

        # 2) Click the country dropdown trigger (+20 with arrow)
        dropdown_trigger = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'phone-code')]"))
        )
        dropdown_trigger.click()
        print("🌍 Opened country dropdown")

        # 3) Pick Malaysia (example)
        malaysia_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Malaysia']/ancestor::li"))
        )
        malaysia_option.click()
        print("✅ Selected Malaysia (+60)")

        # 4) Type phone number
        phone_input = wait.until(
            EC.presence_of_element_located((By.ID, "fm-sms-login-id"))
        )
        phone_input.clear()
        phone_input.send_keys(number[2:])
        print(f"📱 Entered phone number: {number}")

        # 5) Click "Get Code"
        get_code_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='send-btn']/a"))
        )
        get_code_btn.click()
        print("📩 Clicked Get Code")

        wait_until_timeout_or_closed(driver, duration=30)
        numbers_manager.check_number(number_id, number)
    except TimeoutException:
        print("⏳ Timeout waiting for an element")

    finally:
        print("🛑 Closing browser for this number...")
        driver.quit()
    

