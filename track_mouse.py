# import pyautogui
# import time
# import json

# print("🖱️ Move your mouse. Press 'Esc' to stop recording.")

# data = []
# start_time = time.time()

# try:
#     while True:
#         x, y = pyautogui.position()
#         t = time.time() - start_time
#         data.append({'x': x, 'y': y, 't': round(t, 4)})

#         time.sleep(0.01)  # record every 10ms

# except KeyboardInterrupt:
#     print("\nStopped manually.")

# # Save to file
# with open("mouse_recording.json", "w") as f:
#     json.dump(data, f, indent=2)

# print(f"✅ Recorded {len(data)} points. Saved to mouse_recording.json")

import json
import time
import pyautogui

def replay_mouse_drag(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    if not data:
        print("No data to replay.")
        return

    # Move to start position
    start = data[0]
    pyautogui.moveTo(start['x'], start['y'])
    pyautogui.mouseDown()

    start_time = start['t']
    for i in range(1, len(data)):
        point = data[i]
        prev = data[i - 1]

        # Wait the exact time between steps
        delay = point['t'] - prev['t']
        # time.sleep(max(delay, 0))

        pyautogui.moveTo(point['x'], point['y'])

    pyautogui.mouseUp()
    print("Drag complete.")

# Usage
replay_mouse_drag("mouse_recording.json")
