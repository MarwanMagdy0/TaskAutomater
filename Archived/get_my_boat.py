import requests

url = "https://www.getmyboat.com/api/v4/auth/registration/"

session = requests.Session()

# Headers
session.headers.update({
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
    "Content-Type": "application/json",
    "Origin": "https://www.getmyboat.com",
    "Referer": "https://www.getmyboat.com/s/auth/register/agreement/",
    "Sec-CH-UA": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Linux"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-CSRFToken": "sN8mt1jWMN009dS25Rs1hd6HMjyIApZB",
    "X-React-Version": "e8cd189"
})

# Set cookies manually
session.cookies.update({
    "preferred_currency": "USD",
    "__ssid": "8409a9fff3cefd308a2b10256e79b0b",
    "FPID": "FPID2.2.UW4MfmGwZlXfht6daxMs3s0IwWtojRbvz2wk4Fo08gM=.1753195329",
    "FPLC": "lUESlDqan+jY+LAEVpFIVTEA63KirgBZauVjP0j44zL0BY/KzdOw+WUFqPFCJ5Mv23M7PxcxAN4VzrHOpSTF2CXd6SgweK4h+EKCmntqA3Zc/zEKshzPICN2EN1Nlw==",
    "csrftoken": "sN8mt1jWMN009dS25Rs1hd6HMjyIApZB",
    # Include others if necessary
})

# Registration payload
payload = {
    "terms_agreed": True,
    "first_name": "Marwan",
    "last_name": "Magdy",
    "email": "ninisbaddh994@cristoasdut.com",
    "marketing_consent": True,
    "password1": "$j2kDcAy_i_QH_M",
    "password2": "$j2kDcAy_i_QH_M",
    "phone": "+258820643203"
}

# POST request
response = session.post(url, json=payload)

# Output result
print("Status Code:", response.status_code)
print("Response Body:", response.text)
