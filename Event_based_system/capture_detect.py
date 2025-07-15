import cv2
import numpy as np
import time
from mss import mss
sct = mss()
def screen_template_match(template_path, timeout=5, threshold=0.8):
    """
    Blocking function: captures full screen and matches template until timeout or success.

    Args:
        template_path (str): Path to template image.
        timeout (float): Max time in seconds to wait.
        threshold (float): Match confidence threshold.

    Returns:
        (bool, (int, int)|None): (True and center (x, y)) if template found, (False, None) if timeout.
    """
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise ValueError("Template image not found or invalid.")

    w, h = template.shape[::-1]
    
    monitor = sct.monitors[1]  # Full primary monitor (you can loop for multi-monitor support)

    start_time = time.time()
    while time.time() - start_time < timeout:
        screenshot = np.array(sct.grab(monitor))
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            match_x = max_loc[0] + w // 2
            match_y = max_loc[1] + h // 2
            return True, (match_x, match_y)

        time.sleep(0.05)

    return False, None

# Example usage
if __name__ == "__main__":
    template_path = r"DHL_IMGS\button.png"
    timeout = 10

    found, coords = screen_template_match(template_path, timeout)
    if found:
        print("Template found at center:", coords)
    else:
        print("Template not found within timeout.")
