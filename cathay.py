from Archived.Event_based_system.mouse_keyboard import double_click_mouse, scroll_mouse, click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from Archived.Event_based_system import click_image
from utiles import NumbersManager
import pyautogui
from Archived.Event_based_system.fake_data import random_email
import time

country_code_img = "Archived/IMGS/cathay/country_selection.png"
number_field_img = "Archived/IMGS/cathay/number_field.png"
maintenant_button_img = "Archived/IMGS/cathay/maintenant_button.png"
nom_img = "Archived/IMGS/cathay/nom.png"
lname_img = "Archived/IMGS/cathay/lname.png"
date_img = "Archived/IMGS/cathay/date.png"
email_img = "Archived/IMGS/cathay/email.png"
continue_button_img = "Archived/IMGS/cathay/continue_button.png"
close_button_img = "Archived/IMGS/cathay/close.png"
civility_img = "Archived/IMGS/cathay/civility.png"
sms_img = "Archived/IMGS/cathay/sms.png"
password_img = "Archived/IMGS/cathay/password.png"
accept_img = "Archived/IMGS/cathay/accept.png"
accept2_img = "Archived/IMGS/cathay/accept2.png"
verify_img = "Archived/IMGS/cathay/verify.png"
settings_img = "Archived/IMGS/cathay/settings.png"
cookies_img = "Archived/IMGS/cathay/cookies.png"
cookies2_img = "Archived/IMGS/cathay/cookies2.png"
delete_img = "Archived/IMGS/cathay/delete.png"
done_img = "Archived/IMGS/cathay/done.png"
reload_img = "Archived/IMGS/cathay/reload.png"
wait_img = "Archived/IMGS/cathay/wait.png"

numbers_manager = NumbersManager("database/cathay_database.db")

while True:
    number_id, number = numbers_manager.get_available_number()
    print(f"[{number_id}]:{number}")

    click_image(number_field_img)
    type_text(number[2:])
    ret, pos = click_image(country_code_img)
    click_mouse(pos[0], pos[1])
    click_mouse(pos[0], pos[1])
    type_text("indo")
    press_key("enter", 1)
    press_key("enter", 1)
    time.sleep(1)
    click_image(maintenant_button_img)

    click_image(civility_img)
    press_key("enter")
    time.sleep(0.25)

    click_image(nom_img)
    type_text("Wadyelnil")
    time.sleep(0.25)

    click_image(lname_img)
    type_text("Wadyelnil")
    time.sleep(0.25)

    click_image(date_img)
    type_text("02032000")
    time.sleep(0.25)

    click_image(email_img)
    time.sleep(0.25)
    type_text("asdoiqwueo@asoidua.qweqweasd")
    click_image(close_button_img)
    click_image(continue_button_img)
    time.sleep(0.25)

    for i in range(2):
        click_image(sms_img)

    time.sleep(0.25)
    click_image(continue_button_img)
    time.sleep(0.25)

    click_image(password_img)
    type_text("1475asdASD!")
    click_image(accept2_img)
    click_image(verify_img)
    ret_wait, pos = screen_template_match(wait_img, 20)
    click_image(settings_img)
    click_image(cookies_img)
    click_image(cookies2_img)
    while True:
        ret, pos = screen_template_match(delete_img, 1)
        if not ret:
            break

        click_mouse(pos[0], pos[1])
    
    click_image(done_img)
    click_image(reload_img)
    if ret_wait:
        numbers_manager.check_number(number_id, number)