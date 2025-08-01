import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start undetected Chrome
print("[INFO] Launching Chrome...")
driver = uc.Chrome()
wait = WebDriverWait(driver, 30)

try:
    print("[INFO] Opening https://exoticacharters.com/")
    driver.get("https://exoticacharters.com/")

    # Step 1: Click "Get Started"
    print("[INFO] Waiting for 'Get Started' button...")
    get_started = wait.until(EC.element_to_be_clickable((By.ID, "menu_tf")))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", get_started)
    time.sleep(1)
    try:
        get_started.click()
        print("[SUCCESS] Clicked 'Get Started'")
    except:
        driver.execute_script("arguments[0].click();", get_started)
        print("[SUCCESS] Clicked 'Get Started' via JS")

    # Step 2: Click "OK" button by visible text
    print("[INFO] Waiting for 'OK' button by text...")
    ok_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='OK']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", ok_button)
    time.sleep(1)
    try:
        ok_button.click()
        print("[SUCCESS] Clicked 'OK'")
    except:
        driver.execute_script("arguments[0].click();", ok_button)
        print("[SUCCESS] Clicked 'OK' via JS")

    # Step 3: Click "Next" arrow
    print("[INFO] Waiting for 'Next' (arrow) button...")
    next_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='fixed-footer-navigation-next']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_button)
    time.sleep(1)
    try:
        next_button.click()
        print("[SUCCESS] Clicked 'Next'")
    except:
        driver.execute_script("arguments[0].click();", next_button)
        print("[SUCCESS] Clicked 'Next' via JS")

except Exception as e:
    print("[ERROR] Something went wrong:", e)

# Keep browser open for a while to inspect
time.sleep(10)
driver.quit()


