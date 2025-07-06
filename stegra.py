from Event_based_system.get_col import read_column_fast
from Event_based_system.mouse_keyboard import click_mouse, type_text, press_key
from Event_based_system.capture_detect import screen_template_match
from Event_based_system.fake_data import random_email
import time

CHECK = "IMGS/STEGRA_IMGS/check.png"
CONFIRM = "IMGS/STEGRA_IMGS/confirm.png"
COUNTRY = "IMGS/STEGRA_IMGS/country.png"
FNAME = "IMGS/STEGRA_IMGS/fname.png"
LNAME = "IMGS/STEGRA_IMGS/lname.png"
MAIL = "IMGS/STEGRA_IMGS/mail.png"
PNUM = "IMGS/STEGRA_IMGS/pnum.png"
REFRESH = "IMGS/STEGRA_IMGS/refresh.png"
DONE = "IMGS/STEGRA_IMGS/done.png"
FLAG_IMG = "IMGS/STEGRA_IMGS/Slovenia.png"
ERR = "IMGS/STEGRA_IMGS/err.png"
numbers = read_column_fast('/home/marwan/Downloads/new_selvinia_numbers.csv', 'Number')
start = 16
for idx, number in enumerate(numbers[start:]):
    print(idx + start, "====",number)
    ret, pos = screen_template_match(FNAME, 60, 0.8)
    if not ret:
        print("Sign up button not found. Retrying...")
        continue

    click_mouse(pos[0], pos[1])
    type_text("jkasdlkfj", 0.01)
    
    ret, pos = screen_template_match(LNAME, 5, 0.8)
    if not ret:
        continue

    click_mouse(pos[0], pos[1])
    type_text("Slovenia", 0.01)

    ret, pos = screen_template_match(PNUM, 5, 0.8)
    if not ret:
        continue

    click_mouse(pos[0], pos[1])
    type_text("+386", 0.1)
    press_key("enter")
    type_text(number, 0.1)

    ret, pos = screen_template_match(ERR, 1, 0.8)
    if ret:
        ret, pos = screen_template_match(REFRESH, 5, 0.8)
        if not ret:
            print("Done loading not found. Retrying...")
            continue

        click_mouse(pos[0], pos[1])
        time.sleep(1)
        continue

    ret, pos = screen_template_match(MAIL, 5, 0.8)
    if not ret:
        continue

    click_mouse(pos[0], pos[1])
    type_text(random_email(), 0.01)
    press_key("enter")

    ret, pos = screen_template_match(COUNTRY, 5, 0.8)
    if not ret:
        continue

    click_mouse(pos[0], pos[1])
    type_text("Slovenia", 0.1)
    
    ret, pos = screen_template_match(FLAG_IMG, 5, 0.8)
    if not ret:
        continue

    click_mouse(pos[0], pos[1])

    for i in range(3):
        ret, pos = screen_template_match(CHECK, 5, 0.8)

        if not ret:
            continue

        click_mouse(pos[0], pos[1])

    ret, pos = screen_template_match(CONFIRM, 5, 0.8)
    if not ret:
        continue

    click_mouse(pos[0], pos[1])

    ret, pos = screen_template_match(DONE, 10, 0.8)
    if not ret:
        continue

    time.sleep(3)
