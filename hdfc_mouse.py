from Archived.Event_based_system.mouse_keyboard import double_click_mouse, click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from utiles import NumbersManager
import pyautogui
from Archived.Event_based_system.fake_data import random_email
import time


numbers = [
    "820540301",
    "826427011",
    "829355008",
    "823515849",
    "824795794",
    "826127627",
    "828350870",
    "826870959",
    "821811742",
    "822643848",
    "821476195",
    "824026678",
    "825487752",
    "826380924",
    "820695440",
    "827857020",
    "824794311",
    "821067657",
    "827031530",
    "821258117",
    "822642144",
    "821691750",
    "825354862",
    "826051465",
    "822110715",
    
]

sub = "ch_"
verify =        f"Archived/IMGS/hdfc/{sub}verify_mobile.png"
change_number = f"Archived/IMGS/hdfc/{sub}change_number.png"
number_input =  f"Archived/IMGS/hdfc/{sub}number_input.png"
for i, number in enumerate(numbers):
    print(f"[{i}] {number}")
    ret, pos = screen_template_match(number_input)
    click_mouse(pos[0]-200, pos[1]+40)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("delete")
    type_text("1")
    # time.sleep(5)
    click_mouse(pos[0]-200, pos[1]+40)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("delete")
    type_text(number)
    # time.sleep(5)
    ret, pos = screen_template_match(verify)
    
    click_mouse(pos[0], pos[1])

    ret, pos = screen_template_match(change_number)
    click_mouse(pos[0], pos[1])

    time.sleep(1)

    i +=1
    if i == len(numbers):
        i = 0
    
