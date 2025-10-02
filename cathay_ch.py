import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from utiles import NumbersManager
import shutil, time, re, random

URL = "https://www.cathaypacific.com/cx/fr_FR/membership/sign-up.html"

chrome_path = shutil.which("google-chrome") or shutil.which("chromium-browser") or "google-chrome"
numbers_manager = NumbersManager("database/cathay_database.db")

# --- Helper functions for human-like behavior ---
def human_typing(element, text, delay_range=(0.08, 0.2)):
    """Type text like a human, char by char."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(*delay_range))

def human_click(element, delay_range=(0.3, 0.9)):
    """Click with a small random delay like a user."""
    time.sleep(random.uniform(*delay_range))
    element.click()

def human_pause(min_t=0.5, max_t=1.5):
    """Random pause between actions."""
    time.sleep(random.uniform(min_t, max_t))


while True:
    number_id, number = numbers_manager.get_available_number()
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
        human_pause(3, 6)

        dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mpos_dropdown-select__control")))
        human_click(dropdown)
        print("✅ Clicked country code dropdown")

        input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='react-select-'][id$='-input']")))
        human_typing(input_box, f"+{number[:2]}")
        input_box.send_keys(Keys.ENTER)
        print(f"✅ Selected country code +{number[:2]}")

        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phoneNumber")))
        human_typing(phone_input, number[2:])
        print(f"✅ Entered phone number: {number}")

        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary")))
        human_click(submit_btn)
        print("✅ Clicked submit button")

        human_pause(2, 4)

        close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ot-overlay-close")))
        human_click(close_btn)
        print("✅ Closed overlay popup")

        civilite_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mpos_dropdown-select__control")))
        human_click(civilite_dropdown)
        print("✅ Opened 'Civilité' dropdown")

        option_m = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'mpos_dropdown-select__option') and text()='M.']")))
        human_click(option_m)
        print("✅ Selected 'M.'")

        nom_input = wait.until(EC.presence_of_element_located((By.NAME, "familyName")))
        human_typing(nom_input, "Dupont")
        print("✅ Entered last name: Dupont")

        prenom_input = wait.until(EC.presence_of_element_located((By.NAME, "givenName")))
        human_typing(prenom_input, "Jean Michel")
        print("✅ Entered first name: Jean Michel")

        dob_input = wait.until(EC.presence_of_element_located((By.NAME, "birthDate")))
        human_typing(dob_input, "01/01/1990")
        print("✅ Entered date of birth: 01/01/1990")

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "emailAddress")))
        human_typing(email_input, "jean.dupont@example.com")
        print("✅ Entered email: jean.dupont@example.com")

        continuer_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary")))
        human_click(continuer_btn)
        print("✅ Clicked 'Continuer'")

        target_div = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#spa-root > div > div.aem-container.aem-Grid.aem-Grid--12.aem-Grid--default--12 > div:nth-child(3) > div.aem-container.aem-Grid.aem-Grid--12.aem-Grid--default--12 > div > div.mpop.mpop_sign-up > div:nth-child(2) > div > div > div.mpo_main-container > form > div.mpo_form-container > div > div > div:nth-child(2) > div > div > p > div > div > div")))
        human_click(target_div)
        print("✅ Clicked target div")

        continuer_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary[aria-label='Continuer']")))
        human_click(continuer_btn)
        print("✅ Clicked 'Continuer' again")

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        human_typing(password_input, "1475asdASD!")
        print("✅ Entered password")

        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mpo_square-box")))
        human_click(checkbox)
        print("✅ Clicked checkbox")

        verify_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary[aria-label='Vérifier le numéro de téléphone portable']")))
        human_click(verify_btn)
        print("✅ Clicked verify button")

        print("⏳ Waiting 30s for captcha/manual check...")
        time.sleep(30)

        try:
            human_click(verify_btn)
            print("🔁 Retried verify button")
        except:
            print("⚠️ Retry verify button failed")

        numbers_manager.check_number(number_id, number)
        time.sleep(5)

    except TimeoutException:
        print("⏳ Timeout waiting for element")
    except Exception as e:
        print(f"⚠️ Error occurred: {e}")
    finally:
        print("🛑 Closing browser for this number...")
        driver.quit()
