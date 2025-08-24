import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utiles import NumbersManager
import shutil, time

def wait_for_start():
    while True:
        try:
            with open("start.txt", "r") as f:
                content = f.read().strip()
                if content == "1":
                    print("▶ start.txt contains 1, breaking loop.")
                    break
        except FileNotFoundError:
            # create the file with default 0 if it doesn't exist
            with open("start.txt", "w") as f:
                f.write("0")
        time.sleep(0.1)


URL = "https://osappsext.hdfc.com/spotoffer_fe/BasicInformation"

numbers_manager = NumbersManager("database/hdfc_database.db")

chrome_path = shutil.which("google-chrome") or shutil.which("chromium-browser") or "google-chrome"

opts = uc.ChromeOptions()
opts.add_argument("--disable-blink-features=AutomationControlled")
opts.add_argument("--start-maximized")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")

driver = uc.Chrome(
    options=opts,
    version_main=138,                    # match your Chrome 138
    browser_executable_path=chrome_path
)
wait = WebDriverWait(driver, 20)

try:
    driver.get(URL)

    # 1) Mobile number input
    while True:
        wait_for_start()
        number_id, number = numbers_manager.get_available_number()
        mobile = wait.until(EC.presence_of_element_located((By.ID, "b6-MobileNumber_NRI")))
        # Clear and type (use JS to ensure any frameworks get input/change events)
        mobile.clear()
        mobile.click()
        mobile.send_keys("1")

        mobile.clear()
        mobile.click()
        mobile.send_keys(number[3:])
        driver.execute_script("""
            const el = arguments[0];
            el.value = arguments[1];
            el.dispatchEvent(new Event('input', {bubbles: true}));
            el.dispatchEvent(new Event('change', {bubbles: true}));
        """, mobile, number)

        # 2) Wait until "Verify Mobile" becomes enabled (no [disabled] attribute) and clickable, then click
        verify_btn = wait.until(EC.presence_of_element_located((By.ID, "b6-VerifyNRIMobileLink2")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b6-VerifyNRIMobileLink2:not([disabled])")))
        # Some UIs still need a tiny delay after enabling
        time.sleep(0.2)
        verify_btn.click()

        # Optional: wait for any post-verify UI change (toast, OTP field, etc.)
        # Example: wait a beat
        time.sleep(0.5)

        # 3) Click "Change Number"
        change_link = wait.until(EC.element_to_be_clickable((By.ID, "b6-ChangeNumberLink4")))
        change_link.click()

        print("✅ Filled, verified, and clicked Change Number.")

except TimeoutException as e:
    print("⏳ Timeout waiting for an element:", e)
finally:
    # Keep open to inspect the state; press Enter to close
    input("Press Enter to close...")
    driver.quit()
