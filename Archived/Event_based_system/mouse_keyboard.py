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
    Drags the mouse from start to end using a human-like curved path.
    """
    x1, y1 = start
    x2, y2 = end

    # Total number of steps (more steps = smoother)
    steps = random.randint(25, 35)
    sleep_interval = duration / steps

    # Random curve control offset
    curve_intensity = random.uniform(0.1, 0.3)  # how strong the arc bends
    control_x = (x1 + x2) / 2 + (y2 - y1) * curve_intensity
    control_y = (y1 + y2) / 2 + (x1 - x2) * curve_intensity

    def bezier(t, p0, p1, p2):
        return (1 - t)**2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2

    time.sleep(random.uniform(0.05, 0.2))
    pyautogui.mouseDown(x1, y1)

    for i in range(steps + 1):
        t = i / steps
        # ease-in-out (optional, for velocity control)
        t = 3 * t ** 2 - 2 * t ** 3

        xt = bezier(t, x1, control_x, x2)
        yt = bezier(t, y1, control_y, y2)

        # Add small jitter to simulate micro hand movement
        xt += random.uniform(-1.5, 1.5)
        yt += random.uniform(-1.5, 1.5)

        pyautogui.moveTo(xt, yt)

        # Simulate human delay variability
        jitter = random.uniform(0.8, 1.2)
        time.sleep(sleep_interval * jitter)

        # Simulate small pause during long movements
        if i in (int(steps * 0.3), int(steps * 0.7)) and random.random() < 0.3:
            time.sleep(random.uniform(0.05, 0.1))

    time.sleep(random.uniform(0.05, 0.2))
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

def press_key(key, sleep_after=0):
    """
    Presses a key on the keyboard.

    Args:
        key (str): The key to press.
    """
    pyautogui.press(key)
    time.sleep(sleep_after)

if __name__ == "__main__":
    # click_mouse(400, 200)
    type_text("Hello, world!")
    press_key("enter")
    