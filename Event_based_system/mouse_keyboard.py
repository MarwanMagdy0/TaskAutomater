import pyautogui
import time

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
    