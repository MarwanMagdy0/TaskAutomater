import undetected_chromedriver as uc
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from temp_mail import mail_worker
import multiprocessing
from utiles import NumbersManager, EmailManager

parent_conn, child_conn = multiprocessing.Pipe()
p = multiprocessing.Process(target=mail_worker, args=(child_conn,))
p.start()
parent_conn.send("start")
print(">>", parent_conn.recv())
numbers_manager = NumbersManager("database/nike_database.db")
emails_manager = EmailManager("database/nike_database.db")
while True:
    opts = uc.ChromeOptions()
    opts.add_argument("--start-maximized")
    
    driver = uc.Chrome(options=opts, version_main=138)

    driver.get("https://www.nike.com/id/member/settings")

    wait = WebDriverWait(driver, 20)

    # Select country = Costa Rica (CR)
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "country")))
    Select(country_dropdown).select_by_value("CR")

    # Fill Email
    username_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )

    parent_conn.send("get_email")
    msg = parent_conn.recv()
    print(">>", msg)
    email = msg.get("email")
    username_input.clear()
    username_input.send_keys(msg.get("email"))

    # Click Continue
    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="continue"]')))
    continue_btn.click()

    parent_conn.send("get_code")
    msg = parent_conn.recv()
    print(">>", msg)

    otp_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#l7r-code-input")))
    otp_input.clear()
    otp_input.send_keys(msg.get("code"))

    # First name
    first_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#l7r-first-name-input")))
    first_name_input.clear()
    first_name_input.send_keys("John")

    # Last name
    last_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#l7r-last-name-input")))
    last_name_input.clear()
    last_name_input.send_keys("Doe")

    # Password
    password_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#l7r-password-input")))
    password_input.clear()
    password_input.send_keys("StrongPassword123!")
    # keep session for review
    dropdown_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#l7r-shopping-preference"))
    )

    # Wrap with Select
    dropdown = Select(dropdown_element)

    # Select by value
    dropdown.select_by_value("MENS")

    # --- Type Day ---
    day_input = wait.until(EC.element_to_be_clickable((By.ID, "day")))
    day_input.clear()
    day_input.send_keys("15")

    # --- Type Month ---
    month_input = wait.until(EC.element_to_be_clickable((By.ID, "month")))
    month_input.clear()
    month_input.send_keys("08")

    # --- Type Year ---
    year_input = wait.until(EC.element_to_be_clickable((By.ID, "year")))
    year_input.clear()
    year_input.send_keys("1999")

    # Click the checkbox directly 
    try: 
        driver.find_element(By.CSS_SELECTOR, "#privacyTerms").click() 
    except Exception as e: 
        print("Error clicking privacyTerms checkbox directly:", e)

    # Click the Create Account button
    try:
        create_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Create Account"]')))
        create_btn.click()
    except Exception as e:
        print("Error clicking Create Account button:", e)
    
    # save email
    emails_manager.insert_email_with_cookies(email, "StrongPassword123!")

    # Click the Add Mobile Number button
    try:
        add_mobile_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Add Mobile Number"]')))
        add_mobile_btn.click()
    except Exception as e:
        print("Error clicking Add Mobile Number button:", e)

    # Type the phone number
    number_id, number = numbers_manager.get_available_number()
    try:
        phone_input = wait.until(EC.element_to_be_clickable((By.ID, "phoneNumber")))
        phone_input.send_keys(number[2:])  # Skip country code
    except Exception as e:
        print("Error typing phone number:", e)

    try:
        label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='agreeToTerms']")))
        label.click()

    except Exception as e:
        print("Error clicking agreeToTerms checkbox directly:", e)
    
    try:
        send_code_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='send-code-button']")))
        send_code_btn.click()
    except Exception as e:
        print("Error clicking send-code-button directly:", e)

    time.sleep(30)
    numbers_manager.check_number(number_id, number)
    driver.quit()
