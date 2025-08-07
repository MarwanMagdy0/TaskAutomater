import pyautogui
import time, random

def click_mouse(x, y, button='left', duration=0.1):
    """
    Clicks the specified mouse button at (x, y) coordinates.

    Args:
        x (int): X coordinate on screen.
        y (int): Y coordinate on screen.
        button (str): 'left', 'right', or 'middle'.
        delay (float): Delay after the click (seconds).
    """
    pyautogui.moveTo(x, y, duration)
    pyautogui.click(button=button)


def drag_mouse(start, end, duration=1.0):
    """
    Drags mouse from start to end using a human-like curve.
    """
    x1, y1 = start
    x2, y2 = end

    steps = random.randint(5, 10)
    sleep_interval = duration / steps
    time.sleep(random.uniform(0.05, 0.2))
    pyautogui.mouseDown(start[0], start[1])
    for i in range(steps + 1):
        t = i / steps
        # Use ease-in-out curve
        t = 3 * t ** 2 - 2 * t ** 3
        xt = x1 + (x2 - x1) * t + random.uniform(0, 5)
        yt = y1 + (y2 - y1) * t + random.uniform(-10, 10)
        pyautogui.moveTo(xt, yt)
        time.sleep(random.uniform(sleep_interval * 0.8, sleep_interval * 1.2))

    time.sleep(random.uniform(0.05, 0.15))
    pyautogui.mouseUp()

def double_click_mouse(x, y, button='left', duration=0.1):
    """
    Double-clicks the specified mouse button at (x, y) coordinates.

    Args:
        x (int): X coordinate on screen.
        y (int): Y coordinate on screen.
        button (str): 'left', 'right', or 'middle'.
        duration (float): Time to move to the position (seconds).
    """
    pyautogui.moveTo(x, y, duration)
    pyautogui.click(button=button, clicks=2, interval=0.1)

def scroll_mouse(amount, x=None, y=None):
    """
    Scrolls the mouse vertically at the given screen coordinates.

    Args:
        amount (int): Positive to scroll up, negative to scroll down.
        x (int, optional): X coordinate to move to before scrolling.
        y (int, optional): Y coordinate to move to before scrolling.
    """
    if x is not None and y is not None:
        pyautogui.moveTo(x, y)
    pyautogui.scroll(amount)


def type_text(text, interval=0.005):
    """
    Types text with optional delay between characters.

    Args:
        text (str): The text to type.
        interval (float): Delay between each character.
    """
    pyautogui.write(text, interval=interval)

def press_key(key):
    """
    Presses a key on the keyboard.

    Args:
        key (str): The key to press.
    """
    pyautogui.press(key)

if __name__ == "__main__":
    # click_mouse(400, 200)
    type_text("Hello, world!")
    press_key("enter")
    