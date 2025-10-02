from .capture_detect import screen_template_match
from .mouse_keyboard import click_mouse


def click_image(img, timeout = 50, button='left', duration=0.1):
    ret, pos = screen_template_match(img, timeout)
    if ret:
        click_mouse(pos[0], pos[1], button=button, duration=duration)

    return ret, pos
