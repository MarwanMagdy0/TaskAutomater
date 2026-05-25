from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from temp_mail import MailTM
from utiles import NumbersManager
import time

def click_by_text(driver, wait, text):
    element = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, f"label[for='{text}']"))
)

    element.click()
    return element


def fill_by_placeholder(driver, wait, placeholder, value):
    element = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//*[@placeholder={repr(placeholder)}]")
        )
    )
    element.clear()
    element.send_keys(value)
    return element

opts = uc.ChromeOptions()
opts.add_argument("--start-maximized")

driver = uc.Chrome(options=opts)
wait = WebDriverWait(driver, 15)

driver.get("https://www.lynkco.com/en/create-account")

# Accept cookies
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Accept all cookies']")
    )
).click()

time.sleep(3)
driver.switch_to.default_content()

iframes = driver.find_elements(By.ID, "createAccountForm")

print("matching createAccountForm iframes:", len(iframes))

target_iframe = None

for iframe in iframes:
    src = iframe.get_attribute("src") or ""
    if "login.lynkco.com" in src:
        target_iframe = iframe
        break

if target_iframe is None:
    raise Exception("Could not find the real Lynk login iframe")

driver.switch_to.frame(target_iframe)

print("Done switching to real iframe")
country_select = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#otherCountries"))
)


Select(country_select).select_by_value("SI")

country_select = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#countryCode"))
)

mail = MailTM()
email = mail.create_account()

numbers_manager = NumbersManager("database/lynk_database.db")
number_id, number = numbers_manager.get_available_number()


Select(country_select).select_by_value("SI")
# # Fill fields
fill_by_placeholder(driver, wait, "First name", "asdasdasd")
fill_by_placeholder(driver, wait, "Last name", "qweqweqweqwe")
fill_by_placeholder(driver, wait, "Phone number", number)
fill_by_placeholder(driver, wait, "Email", email)
fill_by_placeholder(driver, wait, "Password", "StrongPassword123!")

age_label = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='ageConsent_true']"))
)

age_label.click()

email_label = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='emailSubscribed_true']"))
)

email_label.click()

tos_checkbox = wait.until(
    EC.presence_of_element_located((By.ID, "tosConsent_true"))
)

if not tos_checkbox.is_selected():
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        tos_checkbox
    )

    driver.execute_script("arguments[0].click();", tos_checkbox)


continue_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "continue"))
)

continue_btn.click()

message = mail.wait_for_new_message(timeout=120, interval=5)

print(message)