import requests
import time

BASE_URL = "https://api.mail.tm"

session = requests.Session()

# 1️⃣ Get domain
domain = session.get(f"{BASE_URL}/domains").json()["hydra:member"][0]["domain"]
email = "marwana@" + domain
password = "temp"

print("Email:", email)

# 2️⃣ Create account
res = session.post(f"{BASE_URL}/accounts", json={
    "address": email,
    "password": password
})

if res.status_code not in (200, 201):
    print("Account error:", res.text)
    exit()

# 3️⃣ Get token
token_res = session.post(f"{BASE_URL}/token", json={
    "address": email,
    "password": password
}).json()

token = token_res["token"]

session.headers.update({
    "Authorization": f"Bearer {token}"
})

print("Waiting for messages...\n")

# 4️⃣ Poll inbox
seen = set()

while True:
    inbox = session.get(f"{BASE_URL}/messages").json()["hydra:member"]

    for msg in inbox:
        if msg["id"] in seen:
            continue

        seen.add(msg["id"])

        # Fetch full message
        message = session.get(f"{BASE_URL}/messages/{msg['id']}").json()

        print("📩 NEW MESSAGE")
        print("From:", message["from"]["address"])
        print("Subject:", message["subject"])
        print("Text:", message["text"])
        print("-" * 40)

    time.sleep(5)  # wait 5 seconds before checking again
