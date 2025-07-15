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

numbers = list(set([
    # 50239089697, 50250422948, 50246235985, 50246820706, 50257353839,
    # 50231378291, 50240388259, 50240953844, 50258030880, 50247730530,
    # 50237256403, 50240620925, 50232250806, 50258030832, 50245456833,
    # 50246105423, 50233098243, 50246785011, 50238658293, 50230152454,
    # 50245678451, 50246785074, 50249545423, 50253268572, 50257031595,
    # 50233951566, 50240927970, 50257095972, 50230501054, 50230958536,
    # 50246820710, 50253886021, 50248074542, 50240060072, 50249654787,
    # 50240374674, 50246615354, 50240669544,

    # New Guatemala Tigo PN15 numbers
    50253151536, 50258194089, 50245581257, 50230619865, 50253519428,
    50233021395, 50230411561, 50258858521, 50251830463, 50246285005,
    50230245201, 50248358001, 50231698401, 50233391301, 50239142039,
    50253492206, 50231164833, 50251562408, 50253581519
]))


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
