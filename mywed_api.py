import requests

url = "https://mc.yandex.com/clmap/85845160"
params = {
    "page-url": "https://mywed.com/en/user/edit/",
    "pointer-click": "rn:748251229:x:57752:y:25022:t:2058:p:?*A1AA1:X:635:Y:607",
    "browser-info": "u:1753874382595562931:v:2140:vf:1070pi7qlp4vfntjtgjtz8rq0bae3:rqnl:1:st:1753875135",
    "t": "gdpr(14)ti(1)"
}

headers = {
    "authority": "mc.yandex.com",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
    "cookie": "yandexuid=2489261141752574529; yuidss=2489261141752574529; i=sYtjVmyN9lfR5JDratpdj2wF8L6CcjZUZTMGcCbKQotFXqluIlseRbcCd+4GXajrYh+lHBtyBjPsFOjTZGYAeBxeF+s=; yp=1753954893.yu.4619703601752669032; ymex=1756460493.oyu.4619703601752669032#2068029032.yrts.1752669032#2068029032.yrtsi.1752669032; sync_cookie_ok=synced; yabs-sid=1607744591753868493; receive-cookie-deprecation=1; bh=EkAiTm90KUE7QnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEzOCIsICJHb29nbGUgQ2hyb21lIjt2PSIxMzgiGgN4ODYiDjEzOC4wLjcyMDQuMTAwKgI/MDoHIkxpbnV4IkIGNS4xNS4wSgI2NFJaIk5vdClBO0JyYW5kIjt2PSI4LjAuMC4wIiwiQ2hyb21pdW0iO3Y9IjEzOC4wLjcyMDQuMTAwIiwiR29vZ2xlIENocm9tZSI7dj0iMTM4LjAuNzIwNC4xMDAiYPCDqMQGahncyumIDvKst6UL+/rw5w3r//32D4rUzYcI",
    "origin": "https://mywed.com",
    "referer": "https://mywed.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-cookie-deprecation": "label_only_2",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-fetch-storage-access": "active",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, params=params)

print("Status Code:", response.status_code)
print("Content Length:", len(response.content))
print("Content Type:", response.headers.get("Content-Type"))
