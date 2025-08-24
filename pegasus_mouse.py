from Archived.Event_based_system.mouse_keyboard import double_click_mouse, click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from Archived.Event_based_system import click_image
from utiles import NumbersManager
import pyautogui
from Archived.Event_based_system.fake_data import random_email
import time
from faker import Faker

faker = Faker()

start_img = "Archived/IMGS/pegauses/start.png"
name_img = "Archived/IMGS/pegauses/name.png"
surname_img = "Archived/IMGS/pegauses/surname.png"
num_img = "Archived/IMGS/pegauses/num.png"
sn_img = "Archived/IMGS/pegauses/sn.png"
email_img = "Archived/IMGS/pegauses/email.png"
check_img = "Archived/IMGS/pegauses/check.png"
kabul_img = "Archived/IMGS/pegauses/kabul.png"
click_captcha_img = "Archived/IMGS/pegauses/click_captcha.png"
done_captcha_img = "Archived/IMGS/pegauses/done_captcha.png"
confirm_img = "Archived/IMGS/pegauses/confirm.png"

settings_img = "Archived/IMGS/cathay/settings.png"
cookies_img = "Archived/IMGS/cathay/cookies.png"
cookies2_img = "Archived/IMGS/cathay/cookies2.png"
delete_img = "Archived/IMGS/cathay/delete.png"
done_img = "Archived/IMGS/cathay/done.png"
reload_img = "Archived/IMGS/cathay/reload.png"

numbers = [
    "221764438030",
    "221765996022",
    "221761254230",
    "221761036157",
    "221766273451",
    "221764369834",
    "221765878649",
    "221765530391",
    "221767930610"
    
    
]

for number in numbers:
    screen_template_match(start_img)
    click_image(kabul_img, 10)

    click_image(name_img)
    type_text(faker.user_name())

    click_image(surname_img)
    type_text(faker.last_name())

    _, num_pos = click_image(num_img)
    type_text("221")

    click_image(sn_img)

    click_mouse(num_pos[0] + 80, num_pos[1])
    type_text("76")
    click_mouse(num_pos[0] + 150, num_pos[1])
    type_text(number[5:])

    click_image(email_img)
    type_text(faker.email())

    for _ in range(3):
        time.sleep(0.25)
        click_image(check_img)

    click_image(click_captcha_img)
    screen_template_match(done_captcha_img, 60)

    click_image(confirm_img)

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