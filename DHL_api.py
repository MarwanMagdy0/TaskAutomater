# import requests

# url = "https://shipnow.dhl.com/pwa/service/registration/validateUserMobileNumber?appVersion=2.3.0"

# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Authorization": "Bearer MtS6uHNcIM295BPaJGa83NF0VNDO3w",  # ⚠️ Replace with valid token
#     "Content-Type": "application/json",
#     "Origin": "https://shipnow.dhl.com",
#     "Referer": "https://shipnow.dhl.com/",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
#     "UIClient": "PWA"
# }

# payload = {
#     "mobileNo": "3350686",
#     "countryCode": "LB",
#     "UIClient": "PWA"
# }

# response = requests.post(url, json=payload, headers=headers)

# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())

# import requests
# import json

# url = "https://shipnow.dhl.com/pwa/service/registration/user_getpinV3?appVersion=2.3.0"

# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Authorization": "Bearer MtS6uHNcIM295BPaJGa83NF0VNDO3w",  # ⚠️ Replace if expired
#     "Content-Type": "application/json",
#     "Origin": "https://shipnow.dhl.com",
#     "Referer": "https://shipnow.dhl.com/",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
#     "UIClient": "PWA"
# }

# # This data is likely AES or base64-encoded
# payload = {
#     "iv": "NGQwNGZjY2VhZjYwNGNmMQ==",
#     "state": "7JB6iXPHRs0pwvxddLTPGQ==",
#     "device_info": {
#         "device_language": "en",
#         "device_unique_id": "420b917a-708c-488e-bd1c-cf24d5e8b969",
#         "os_version": "Firefox-136",
#         "time_zone": "GMT+03:00",
#         "rooted": False,
#         "app_id": "com.dhl.exp.dhleapp"
#     },
#     "user_info": {
#         "country": "LB",
#         "language": "en",
#         "phone_number": "7JB6iXPHRs0pwvxddLTPGQ==",  # ⚠️ Appears encrypted
#         "first_name": "asdasd asdsad"
#     },
#     "captchaVerificationData": {
#         "captchaText": "",
#         "token": ""
#     },
#     "appVersion": "2.3.0",
#     "timezoneOffset": "+03:00",
#     "UIClient": "PWA"
# }

# response = requests.post(url, headers=headers, json=payload)

# # Output result
# print("Status Code:", response.status_code)
# try:
#     print("Response JSON:", response.json())
# except Exception:
#     print("Response Text:", response.text)
#!/usr/bin/env python3
import pyautogui
import time

print("Auto-clicker started. Press Ctrl+C to stop.")

try:
    while True:
        pyautogui.click()  # Left click at current mouse position
        print("Clicked at", time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(60)  # Wait for 60 seconds
except KeyboardInterrupt:
    print("Stopped by user.")
