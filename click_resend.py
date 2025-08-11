from Archived.Event_based_system.mouse_keyboard import click_mouse, drag_mouse
from Archived.Event_based_system.capture_detect import screen_template_match
import time, os
resend_img =  f"Archived/IMGS/cainiao/Resend.png"
resend_img2 =  f"Archived/IMGS/cainiao/resend2.png"
slider = f"Archived/IMGS/cainiao/slider.png"
slider2 = f"Archived/IMGS/cainiao/slider2.png"
error = f"Archived/IMGS/cainiao/error.png"
while True:
    ret, pos = screen_template_match(resend_img, 0.1)
    if ret:
        time.sleep(1)
        click_mouse(pos[0], pos[1])
    
    ret, pos = screen_template_match(resend_img2, 0.1)
    if ret:
        time.sleep(1)
        click_mouse(pos[0], pos[1])
        time.sleep(5)
    
    ret, pos = screen_template_match(slider, 0.1)
    if ret:
        os.system("play -nq -t alsa synth 0.1 sine 1000")
        time.sleep(1)
    

    ret, pos = screen_template_match(slider2, 0.1)
    if ret:
        os.system("play -nq -t alsa synth 0.1 sine 1000")
        time.sleep(1)
    
    ret, pos = screen_template_match(error, 0.1)
    if ret:
        os.system("play -nq -t alsa synth 0.1 sine 1000")
        time.sleep(1)



# 601159732248
# 601156758991
# 60103351727
# 60103022959