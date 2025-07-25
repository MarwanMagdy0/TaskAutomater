from Event_based_system.get_col import read_column_fast
from Event_based_system.mouse_keyboard import click_mouse, type_text, press_key, double_click_mouse
from Event_based_system.capture_detect import screen_template_match
from Event_based_system.fake_data import random_email
import time

VERIFY_IMG = 'IMGS/boatbooker/verify.png'
OK_IMG = 'IMGS/boatbooker/ok.png'
CANCEL_IMG = 'IMGS/boatbooker/cancel.png'
LINEEDIT_IMG = 'IMGS/boatbooker/lineedit.png'
SAVE_IMG = 'IMGS/boatbooker/save.png'
BLUE_OK_IMG = 'IMGS/boatbooker/blue_ok.png'

# numbers = read_column_fast('/home/marwan/Downloads/IMS SMS  My SMS Numbers.csv', 'Number')

numbers = [
    258822220402, 258828759960, 258826627438, 258823543928, 258825643454,
    258821161461, 258828182416, 258826880271, 258822798960, 258820913809,
    258823620732, 258823128450, 258824237571, 258825495892, 258827685552,
    258829142413, 258824164252, 258820283199, 258820729631
]



print("Total numbers:", len(numbers))
i = 0
while True:
    if i >= len(numbers):
        print("All numbers processed. Exiting.")
        i = 0
    phone_number = str(numbers[i])
    print(f"[{i}] Iteration:", phone_number)
    # Wait for the line edit field to appear
    ret, pos = screen_template_match(LINEEDIT_IMG, 5, 0.8)
    if not ret:
        print("Line edit field not found. Retrying...")
        continue

    double_click_mouse(pos[0], pos[1])
    type_text(phone_number)

    # Wait for the Save button to appear
    ret, pos = screen_template_match(SAVE_IMG, 5, 0.8)
    if not ret:
        print("Save button not found. Retrying...")
        continue

    click_mouse(pos[0], pos[1], duration=0.5)


    time.sleep(25)
    ret, pos = screen_template_match(VERIFY_IMG, 5, 0.8)
    if not ret:
        print("Verification image not found. Retrying...")
        continue

    click_mouse(pos[0], pos[1])
    
    # Wait for the OK button to appear
    ret, pos = screen_template_match(OK_IMG, 5, 0.8)
    if not ret:
        print("OK button not found. Retrying...")
        continue

    click_mouse(pos[0], pos[1],duration= 0.5)
    time.sleep(1)
    # Wait for the Cancel button to appear
    ret, pos = screen_template_match(CANCEL_IMG, 1, 0.8)
    if not ret:
        print("Cancel button not found. Retrying...")
        # Wait for the Blue OK button to appear
        ret, pos = screen_template_match(BLUE_OK_IMG, 2, 0.8)
        if not ret:
            print("Blue OK button not found. Retrying...")
            continue

        click_mouse(pos[0], pos[1], duration=0.5)
        continue

    click_mouse(pos[0], pos[1], duration=0.5)
    i += 1
