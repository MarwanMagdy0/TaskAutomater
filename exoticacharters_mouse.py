from Archived.Event_based_system.mouse_keyboard import click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from utiles import NumbersManager
from Archived.Event_based_system.fake_data import random_email
import time
# https://exoticacharters.com/
get_started = "Archived/IMGS/get_started.png"
ok = "Archived/IMGS/ok.png"
type1 = "Archived/IMGS/type1.png"
usa = "Archived/IMGS/usa.png"
number_img = "Archived/IMGS/number_gua.png"
submit = "Archived/IMGS/submit.png"
back = "Archived/IMGS/back.png"

numbers_manager = NumbersManager("database/exotic_database.db")

while True:
    number_id, number = numbers_manager.get_available_number()
    ret, pos = screen_template_match(get_started, 60, 0.8)
    if not ret:
        print("Get Started button not found. Retrying...")

    time.sleep(2)
    click_mouse(pos[0], pos[1])


    for i in range(8):
        time.sleep(0.7)
        ret, pos = screen_template_match(ok, 60, 0.8)
        if not ret:
            print("OK button not found. Retrying...")

        click_mouse(pos[0], pos[1])

    time.sleep(0.7)

    # email = random_email()
    type_text("asdjaskld", 0.1)
    press_key('enter')
    time.sleep(0.7)
    ret, pos = screen_template_match(ok, 60, 0.8)
    if not ret:
        print("OK button not found. Retrying...")

    click_mouse(pos[0], pos[1])

    time.sleep(0.7)
    type_text("asdjaskld", 0.1)
    press_key('enter')
    time.sleep(1)

    type_text(random_email(), 0.1)
    press_key('enter')
    time.sleep(0.7)

    ret, pos = screen_template_match(usa, 5, 0.8)
    if not ret:
        print("usa button not found. Retrying...")
    click_mouse(pos[0], pos[1])
    time.sleep(1)
    type_text("guatema", 0.1)

    press_key('enter')

    ret, pos = screen_template_match(number_img, 5, 0.8)
    if not ret:
        print("Number input not found. Retrying...")

    click_mouse(pos[0], pos[1])
    time.sleep(0.7)
    type_text(number, 0.1)

    press_key('enter')

    ret, pos = screen_template_match(submit, 5, 0.8)
    if not ret:
        print("Submit button not found. Retrying...")

    click_mouse(pos[0], pos[1])

    time.sleep(5)
    ret, pos = screen_template_match(back, 5, 0.8)
    if not ret:
        print("Back button not found. Retrying...")
    click_mouse(pos[0], pos[1])
