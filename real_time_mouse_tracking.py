import pyautogui
import time

def track_mouse(interval=0.05):
    """
    Continuously prints the current mouse position.

    Args:
        interval (float): Time (in seconds) between updates.
    """
    print("Press Ctrl+C to stop tracking.\n")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"\rMouse position: ({x}, {y})", end='', flush=True)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nTracking stopped.")

# Run it
if __name__ == "__main__":
    track_mouse()
