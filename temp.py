import requests

# The intent ID
itt = "itt_6961cf3f-d38e-4c32-bab2-6533c13cc98b"

# URL
url = f"https://api.youcanbook.me/v1/intents/{itt}/booking/cancel"

# Headers (replicated from curl)
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
    "content-type": "application/json",
    "origin": "https://book.youcanbook.me",
    "priority": "u=1, i",
    "referer": "https://book.youcanbook.me/",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-browser-id": "1PBR2B1",
    "x-request-id": "BA-FD20H8H",
    "x-session-id": "AITQ407"
}

# Cookies (from curl)
cookies = {
    "COOKIE_CONSENT": "1769102646596",
    "yst": "vral",
    "ysi": "maridalsveiensmadyrklinikk",
    "_ga": "GA1.1.1028421081.1769102647",
    "_hjSessionUser_261076": "eyJpZCI6ImY5MDljZTBjLTg1ZTItNTA0OC1iZjNiLTUyOWFiNjBjZDlmYiIsImNyZWF0ZWQiOjE3NjkxMDI2NDczNjcsImV4aXN0aW5nIjp0cnVlfQ==",
    "_hjSession_261076": "eyJpZCI6IjZkMDc5MDBjLTU1ODEtNGM0Zi1hNzE1LTQ4NzBhMDI1NzVlMSIsImMiOjE3NjkxMTA0MTEwNDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=",
    "_ga_82FV3HE5LC": "GS2.1.s1769102647$o1$g1$t1769111640$j60$l0$h0"
}

# JSON payload
data = {
    "reason": f"https://api.youcanbook.me/v1/intents/itt_3374fdff-76f1-4235-bb14-0e09af5205de/booking/cancel",
    "secret": "510B46"
}

# Make the PATCH request
response = requests.patch(url, headers=headers, cookies=cookies, json=data)

# Print the response
print(response.status_code)
print(response.text)