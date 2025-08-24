import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import shutil, time, re
URL = "https://www.cathaypacific.com/cx/fr_FR/membership/sign-up.html"

numbers = """
Malaysia XOX TF44    601120797175
Malaysia XOX TF44    601157649896
Malaysia XOX TF44    60103095442
Malaysia XOX TF44    601158725953
Malaysia XOX TF44    601159698136
Malaysia XOX TF44    601155618001
Malaysia XOX TF44    60103023587
Malaysia XOX TF44    601157596998
Malaysia XOX TF44    601113113515
Malaysia XOX TF44    601158518717
Malaysia XOX TF44    601159882712
Malaysia XOX TF44    60103355310
Malaysia XOX TF44    601158579775
Malaysia XOX TF44    60103404051
Malaysia XOX TF44    601157772909
Malaysia XOX TF44    60103064588
Malaysia XOX TF44    601157672315
Malaysia XOX TF44    601113224971
Malaysia XOX TF44    60108519626
Malaysia XOX TF44    60103409921
Malaysia XOX TF44    601159799143
Malaysia XOX TF44    601113023847
Malaysia XOX TF44    60103022952
Malaysia XOX TF44    601113198721
Malaysia XOX TF44    601113125470
Malaysia XOX TF44    601159932555
Malaysia XOX TF44    601158502592
Malaysia XOX TF44    601157698721
Malaysia XOX TF44    601155650879
Malaysia XOX TF44    601113166630
Malaysia XOX TF44    601113291342
Malaysia XOX TF44    601113322564
Malaysia XOX TF44    601158587819
Malaysia XOX TF44    601158534221
Malaysia XOX TF44    601157595323
Malaysia XOX TF44    601158536931
Malaysia XOX TF44    601158858670
Malaysia XOX TF44    601157371067
Malaysia XOX TF44    601156898769
Malaysia XOX TF44    601120598896
Malaysia XOX TF44    601156813278
Malaysia XOX TF44    601113041768
Malaysia XOX TF44    601158665524
Malaysia XOX TF44    601113173719
Malaysia XOX TF44    601157887831
Malaysia XOX TF44    601158520398
Malaysia XOX TF44    601159741806
Malaysia XOX TF44    601155184692
Malaysia XOX TF44    601158785389
Malaysia XOX TF44    601113279209

"""
chrome_path = shutil.which("google-chrome") or shutil.which("chromium-browser") or "google-chrome"
extracted_numbers = [num[2:] for num in re.findall(r"\b60\d+\b", numbers)]

for number in extracted_numbers[7:]:
    print(f"\n📱 Using number: {number}")
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
        time.sleep(5)

        dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mpos_dropdown-select__control")))
        dropdown.click()
        print("✅ Clicked country code dropdown")

        input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='react-select-'][id$='-input']")))
        input_box.send_keys("+60")
        input_box.send_keys(Keys.ENTER)
        print("✅ Selected country code +60")

        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phoneNumber")))
        phone_input.send_keys(number)
        print(f"✅ Entered phone number: {number}")

        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary")))
        submit_btn.click()
        print("✅ Clicked submit button")

        time.sleep(3)
        close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ot-overlay-close")))
        close_btn.click()
        print("✅ Closed overlay popup")

        civilite_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mpos_dropdown-select__control")))
        civilite_dropdown.click()
        print("✅ Opened 'Civilité' dropdown")

        option_m = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'mpos_dropdown-select__option') and text()='M.']")))
        option_m.click()
        print("✅ Selected 'M.'")

        nom_input = wait.until(EC.presence_of_element_located((By.NAME, "familyName")))
        nom_input.send_keys("Dupont")
        print("✅ Entered last name: Dupont")

        prenom_input = wait.until(EC.presence_of_element_located((By.NAME, "givenName")))
        prenom_input.send_keys("Jean Michel")
        print("✅ Entered first name: Jean Michel")

        dob_input = wait.until(EC.presence_of_element_located((By.NAME, "birthDate")))
        dob_input.send_keys("01/01/1990")
        print("✅ Entered date of birth: 01/01/1990")

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "emailAddress")))
        email_input.send_keys("jean.dupont@example.com")
        print("✅ Entered email: jean.dupont@example.com")

        continuer_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary")))
        continuer_btn.click()
        print("✅ Clicked 'Continuer'")

        target_div = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#spa-root > div > div.aem-container.aem-Grid.aem-Grid--12.aem-Grid--default--12 > div:nth-child(3) > div.aem-container.aem-Grid.aem-Grid--12.aem-Grid--default--12 > div > div.mpop.mpop_sign-up > div:nth-child(2) > div > div > div.mpo_main-container > form > div.mpo_form-container > div > div > div:nth-child(2) > div > div > p > div > div > div")))
        target_div.click()
        print("✅ Clicked target div")
        time.sleep(2)

        continuer_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary[aria-label='Continuer']")))
        continuer_btn.click()
        print("✅ Clicked 'Continuer' again")

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        password_input.send_keys("1475asdASD!")
        print("✅ Entered password")

        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mpo_square-box")))
        checkbox.click()
        print("✅ Clicked checkbox")

        verify_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mpos_button.mpos_button-primary[aria-label='Vérifier le numéro de téléphone portable']")))
        verify_btn.click()
        print("✅ Clicked verify button")

        print("⏳ Waiting 30s for captcha/manual check...")
        time.sleep(30)

        try:
            verify_btn.click()
            print("🔁 Retried verify button")
        except:
            print("⚠️ Retry verify button failed")
        time.sleep(5)

    except :
        print("⏳ Timeout waiting for element:")
    finally:
        print("🛑 Closing browser for this number...")
        driver.quit()
    
    time.sleep(60)
