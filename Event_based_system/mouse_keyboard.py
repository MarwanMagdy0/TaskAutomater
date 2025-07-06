import pyautogui
import time

def click_mouse(x, y, button='left', delay=0.1):
    """
    Clicks the specified mouse button at (x, y) coordinates.

    Args:
        x (int): X coordinate on screen.
        y (int): Y coordinate on screen.
        button (str): 'left', 'right', or 'middle'.
        delay (float): Delay after the click (seconds).
    """
    pyautogui.moveTo(x, y)
    pyautogui.click(button=button)
    time.sleep(delay)


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
    