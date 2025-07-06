from Event_based_system.get_col import read_column_fast
from Event_based_system.mouse_keyboard import click_mouse, type_text, press_key
from Event_based_system.capture_detect import screen_template_match
from Event_based_system.fake_data import random_email
import time

CHECK_BOX_PATH = r'IMGS/DHL_IMGS/check_box.png'
CONTINUE_BUTTON_PATH = r'IMGS/DHL_IMGS/continue.png'
EMAIL_PATH = r'IMGS/DHL_IMGS/email.png'
FIRST_NAME_PATH = r'IMGS/DHL_IMGS/first_name.png'
LAST_NAME_PATH = r'IMGS/DHL_IMGS/last_name.png'
MOBILE_PATH = r'IMGS/DHL_IMGS/mobile_nm.png'
PASSWORD_PATH = r'IMGS/DHL_IMGS/password.png'
SIGN_UP_1_PATH = r'IMGS/DHL_IMGS/sign_up1.png'
SIGN_UP_2_PATH = r'IMGS/DHL_IMGS/sign_up2.png'
REFRESH_PATH = r'IMGS/DHL_IMGS/refresh_firefox.png'
DONE_LOADING_PATH = r'IMGS/DHL_IMGS/done_loading.png'
TRUE_PATH = r'IMGS/DHL_IMGS/True.png'
# Get numbers from the CSV file
numbers = read_column_fast('Numbers/Senegal/IMS SMS  My SMS Numbers.csv', 'Number')
start = 5
for idx, number in enumerate(numbers[start:]):
    print(idx, "====",number)
    working = True
    while working:
        ret, pos = screen_template_match(SIGN_UP_1_PATH, 5, 0.8)
        if not ret:
            print("Sign up button not found. Retrying...")
            break

        click_mouse(pos[0], pos[1])
        
        # Click on the "Sign up" button
        ret, pos = screen_template_match(SIGN_UP_2_PATH, 5, 0.8)
        if not ret:
            break

        click_mouse(pos[0], pos[1])

        ret, pos = screen_template_match(FIRST_NAME_PATH, 5, 0.8)
        if not ret:
            break

        click_mouse(pos[0], pos[1])
        type_text("Lebanon", 0.01)

        ret, pos = screen_template_match(LAST_NAME_PATH, 5, 0.8)
        if not ret:
            break

        click_mouse(pos[0], pos[1])
        type_text("Alfa", 0.01)

        ret, pos = screen_template_match(MOBILE_PATH, 5, 0.8)
        if not ret:
            break
        
        click_mouse(pos[0], pos[1])
        type_text(number, 0.01)
        
        ret, pos = screen_template_match(EMAIL_PATH, 5, 0.8)
        if not ret:
            break
        
        click_mouse(pos[0], pos[1])

        type_text(random_email(), 0.01)
        press_key("enter")

        ret, pos = screen_template_match(PASSWORD_PATH, 5, 0.8)
        if not ret:
            break
        
        click_mouse(pos[0], pos[1])
        type_text("1238KLKJalkjkasjd*)*&)(*&987)", 0.01)

        ret, pos = screen_template_match(CHECK_BOX_PATH, 5, 0.8)
        if not ret:
            break

        click_mouse(pos[0], pos[1])

        ret, pos = screen_template_match(CONTINUE_BUTTON_PATH, 5, 0.8)
        if not ret:
            break

        click_mouse(pos[0], pos[1])
        
        ret, pos = screen_template_match(TRUE_PATH, 5, 0.8)
        if not ret:
            working = False
            break
    
        time.sleep(3)
    
        ret, pos = screen_template_match(REFRESH_PATH, 10, 0.8)
        if not ret:
            break
        
        click_mouse(pos[0], pos[1])
        time.sleep(1)

        ret, _ = screen_template_match(DONE_LOADING_PATH, 50, 0.8)
        if not ret:
            print("Done loading not found. Retrying...")
            break
    
        working = False

