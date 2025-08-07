from Archived.Event_based_system.mouse_keyboard import click_mouse, drag_mouse
from Archived.Event_based_system.capture_detect import screen_template_match
import time
resend_img =  f"Archived/IMGS/cainiao/Resend.png"
slider = f"Archived/IMGS/cainiao/slider.png"
error = f"Archived/IMGS/cainiao/error.png"
while True:
    ret, pos = screen_template_match(resend_img, 0.1)
    if ret:
        click_mouse(pos[0], pos[1])
    
    ret, pos = screen_template_match(slider, 0.1)
    if ret:
        drag_mouse(pos, [pos[0]+260, pos[1]], duration=0.1)
    
    ret, pos = screen_template_match(error, 0.1)
    if ret:
        click_mouse(pos[0], pos[1])



# 601156832166