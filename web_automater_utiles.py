import threading
import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
import queue
def wait_for_selector(page, selector, timeout=5000):
    try:
        page.wait_for_selector(selector, timeout=timeout)
        return True
    except Exception:
        return False
    


class CaptchaViewer:
    def __init__(self):
        self.queue = queue.Queue()
        self.image = None
        self.root = None
        self.label = None
        self.gui_thread = threading.Thread(target=self._run_gui, daemon=True)
        self.gui_thread.start()

    def _run_gui(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("CAPTCHA Viewer")
        self.root.attributes("-topmost", True)

        self.label = tk.Label(self.root)
        self.label.pack()

        self.root.after(100, self._process_queue)
        self.root.mainloop()

    def _process_queue(self):
        try:
            while True:
                tk_image = self.queue.get_nowait()
                if self.image:
                    del self.image  # cleanup previous image
                self.image = tk_image
                self.label.config(image=self.image)
        except queue.Empty:
            pass
        if self.root:
            self.root.after(100, self._process_queue)

    def update_image(self, url):
        def fetch_image():
            try:
                response = requests.get(url, timeout=5)
                image = Image.open(BytesIO(response.content))
                tk_image = ImageTk.PhotoImage(image)
                self.queue.put(tk_image)
            except Exception as e:
                print(f"Failed to load image: {e}")
        threading.Thread(target=fetch_image, daemon=True).start()
