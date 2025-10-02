from Archived.Event_based_system.mouse_keyboard import double_click_mouse, scroll_mouse, click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from Archived.Event_based_system import click_image
from utiles import NumbersManager
import pyautogui
from Archived.Event_based_system.fake_data import random_email
import time

numbers_manager = NumbersManager("database/hbomax_database.db")

continue_button_img = "Archived/IMGS/hbomax/continue.png"
fname_img = "Archived/IMGS/hbomax/fname.png"
edit_img = "Archived/IMGS/hbomax/edit.png"

while True:
    ret, pos = screen_template_match(continue_button_img, 50)

    click_mouse(pos[0]+150, pos[1] - 120)
    time.sleep(3)
    number_id, number = numbers_manager.get_available_number()
    type_text(number[2:5], 0.5)
    press_key("right")
    press_key("right")
    press_key("right")
    type_text(number[5:], 0.1)

    click_mouse(pos[0], pos[1])

    ret, pos = screen_template_match(fname_img, 50)
    time.sleep(0.5)
    click_mouse(pos[0], pos[1]+50)
    time.sleep(0.5)
    type_text("Wadyelnil", 0.1)

    click_mouse(pos[0], pos[1]+150)
    type_text("asqweqwe", 0.1)
    time.sleep(0.5)
    click_mouse(pos[0], pos[1]+430)

    time.sleep(0.5)
    click_image(edit_img)