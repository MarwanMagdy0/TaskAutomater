import time
import multiprocessing
from playwright.sync_api import Playwright, sync_playwright, TimeoutError

POLL_INTERVAL = 5.0    # seconds between refresh attempts
POLL_TIMEOUT = 60.0    # max seconds to wait for OTP

def mail_worker(conn):
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        email = None

        # Load once
        page.goto("https://www.moakt.com/en")

        while True:
            if not conn.poll(0.1):
                continue

            cmd = conn.recv()

            if cmd == "exit":
                conn.send("bye")
                break

            elif cmd == "start":
                try:
                    page.get_by_role("button", name="Get a Random Address").click(timeout=3000)
                except TimeoutError:
                    pass

                email = page.locator("#email-address").inner_text(timeout=5000).strip()
                conn.send({"status": "ok", "email": email})

            elif cmd == "get_email":
                if email:
                    conn.send({"email": email})
                else:
                    conn.send({"error": "no email yet"})

            elif cmd == "get_code":
                start = time.time()
                code = None
                while time.time() - start < POLL_TIMEOUT:
                    try:
                        no_msg = page.locator("text=No messages in your inbox at the moment.")
                        print("[-] No message:", no_msg.count())
                        if no_msg.count() == 0:
                            # message appeared → open first one
                            print("[+] Message detected, opening it...")
                            page.get_by_role("link", name="Este es tucódigo de un solo uso").click(timeout=3000)
                            iframe_elem = page.locator("iframe").first.element_handle(timeout=5000)
                            frame = iframe_elem.content_frame()
                            message_locator = frame.locator(
                                "body > table > tbody > tr > td > div > table.wrapper.emailContainer "
                                "> tbody > tr:nth-child(4) > td > table > tbody > tr > td > div > "
                                "table > tbody > tr > td > p"
                            )
                            text = message_locator.inner_text(timeout=5000)
                            code = text
                            break
                    except TimeoutError:
                        pass

                    # refresh inbox list
                    try:
                        page.get_by_role("link", name="refresh Refresh List").click(timeout=2000)
                    except TimeoutError:
                        try:
                            page.locator("text=Refresh").first.click(timeout=2000)
                        except TimeoutError:
                            pass

                    time.sleep(POLL_INTERVAL)

                if code:
                    page.locator("a[onclick*='changeAddress']").click(timeout=3000)
                    print("[+] Reloading page to reset state...")
                    page.reload(wait_until="load")
                    conn.send({"code": code})
                else:
                    conn.send({"error": "no code after timeout"})


        context.close()
        browser.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=mail_worker, args=(child_conn,))
    p.start()

    parent_conn.send("start")
    print(">>", parent_conn.recv())

    parent_conn.send("get_email")
    print(">>", parent_conn.recv())

    parent_conn.send("get_code")
    print(">>", parent_conn.recv())

    # parent_conn.send("exit")
    # print(">>", parent_conn.recv())

    # p.join()
