import requests


def parse_cookies(raw_string):
    cookies = {}
    lines = raw_string.strip().splitlines()

    for line in lines:
        line = line.strip()
        if not line or '\t' not in line:
            continue

        key, value = line.split('\t', 1)
        key = key.strip()
        value = value.strip().strip('"')  # remove surrounding quotes

        # skip non-cookie fields
        if key.lower() in {"expires", "path", "secure", "value"}:
            continue

        cookies[key] = value

    return cookies



headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://boatbooker.com/manage/profile",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "X-Requested-With": "XMLHttpRequest"
}

cookie_string = """

_fbp	"fb.1.1752346439356.287063122644941675"
_ga	"GA1.1.987765930.1752346082"
_ga_TT5WXDW45Z	"GS2.1.s1752353599$o2$g1$t1752354676$j59$l0$h743122511"
_gcl_au	"1.1.1590740622.1752346082.787215481.1752346166.1752346246"
_hjHasCachedUserAttributes	"true"
_hjSession_5171925	"eyJpZCI6IjA1YjM4ZjFiLTNhNzMtNDY1NC04NTE5LTE1Y2ExYmUzZDJiOCIsImMiOjE3NTIzNDYwODU4NTQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0="
_hjSessionUser_5171925	"eyJpZCI6IjJhZmFhMDJmLTc0MjUtNTQ4MC1iMmQwLTAxMzhmY2FkMDhjOCIsImNyZWF0ZWQiOjE3NTIzNDYwODU4NTMsImV4aXN0aW5nIjp0cnVlfQ=="
_uetsid	"bd4eb6305f5011f083b0bd17bf7da650"
_uetvid	"bd4ec0b05f5011f0949cf3d7ba7bd08e"
auth_token	"RNtuv6L2C3z4QEmVAmhm"
fbac	"ts= (none) Traffic> l= [No Referer] > tt= [No Referer] Traffic"
FPAU	"1.1.1590740622.1752346082"
geo_currency	"USD"
identity	"asdad@asd.asd"
PHPSESSID	"8ajcheqf1gkgum8l28u7fo4114"
remember_code	"P1816kn2vj87OZc4C3Ru"
session_id	"e9d1391c-5513-4e99-aff2-e547b7cf1a6d"
universal_id	"a378169ec1587bf66d725f9bcf714c26"
"""

cookie_string = """
_fbp	"fb.1.1752346439356.287063122644941675"
_ga	"GA1.1.987765930.1752346082"
_ga_TT5WXDW45Z	"GS2.1.s1752356999$o3$g1$t1752361410$j15$l0$h680285503"
_gcl_au	"1.1.1590740622.1752346082.787215481.1752346166.1752346246"
_hjHasCachedUserAttributes	"true"
_hjSession_5171925	"eyJpZCI6ImE1Nzg0MDgxLTM0NzYtNGJhYi1iZTJhLWY3ZDFjNWJjYTYzYSIsImMiOjE3NTIzNjEzNjU4NTAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0="
_hjSessionUser_5171925	"eyJpZCI6IjJhZmFhMDJmLTc0MjUtNTQ4MC1iMmQwLTAxMzhmY2FkMDhjOCIsImNyZWF0ZWQiOjE3NTIzNDYwODU4NTMsImV4aXN0aW5nIjp0cnVlfQ=="
_uetsid	"bd4eb6305f5011f083b0bd17bf7da650"
_uetvid	"bd4ec0b05f5011f0949cf3d7ba7bd08e"
auth_token	"RNtuv6L2C3z4QEmVAmhm"
bbLandingPage	"manage_profile"
cf_chl_rc_m	"1"
cf_clearance	"9aSjhcLuCf4cat_XcY.8OhHA55WSmd9YZPSt6I2c1.4-1752358393-1.2.1.1-rG5TWp50hUr_h0f2GKlLRmTbtSK1BwhACJI.VuvNJNfuYttQKIQMHjbOkExvJM6xxFkLg4_bgHU2hhFBA3STTIA3kmeevBWyTpqxeZO79PcQweSPnY31f9_AQ9ilW3ve66NTUHUIV9ZR4eTMOeBugvKpCWRdCpN3ZJ9pIW7DCISXT_yMcO_Gy2785waIvPEUaGiVxdJ3aGlXZ7B5P2YyxWcRnojhhoW8.u3aUuClSPQ"
fbac	"ts= (none) Traffic> l= [No Referer] > tt= [No Referer] Traffic"
FPAU	"1.1.1590740622.1752346082"
geo_currency	"USD"
identity	"asdad@asd.asd"
PHPSESSID	"8ajcheqf1gkgum8l28u7fo4114"
remember_code	"P1816kn2vj87OZc4C3Ru"
session_id	"71fed534-5720-474e-83a9-f45c489f714b"
universal_id	"a378169ec1587bf66d725f9bcf714c26"
"""

cookies = parse_cookies(cookie_string)

cookies = {
    "universal_id": "88a709b749b7884f95e34c32443021d1",
    "fbac": "ts= (none) Traffic> l= [No Referer] > tt= [No Referer] Traffic",
    "_gcl_au": "1.1.1558042379.1752400749",
    "_ga": "GA1.1.1012369817.1752400749",
    "FPAU": "1.1.1558042379.1752400749",
    "_hjSessionUser_5171925": "eyJpZCI6IjZhYTI1Y2Q0LTk2OWMtNWY0YS1iYjFiLTA0N2EzNGE4YTE1YyIsImNyZWF0ZWQiOjE3NTI0MDA3NTA0NTMsImV4aXN0aW5nIjp0cnVlfQ==",
    "remember_code": "WG7MzO4fBLZ2jthhWi2f",
    "identity": "maromady99@gmail.com",
    "auth_token": "lhU8bwvFRMEtBflEn2Hg",
    "_hjSession_5171925": "eyJpZCI6ImQ1MTRmNmUyLTg3MjMtNDMzMy1iNDNiLWZlOGZlZTk3ZDczOSIsImMiOjE3NTI0MjI0NjUxMjEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=",
    "OptanonAlertBoxClosed": "2025-07-13T16:03:20.119Z",
    "currency": "SGD",
    "geo_currency": "SGD",
    "session_id": "bf9d24c4-4439-4d3b-8038-d45eba16c629",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Sun+Jul+13+2025+19%3A41%3A18+GMT%2B0300+(Eastern+European+Summer+Time)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=711161bd-eeb1-4aca-84e4-52d95844cb60&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0001%3A1&intType=1&geolocation=GB%3BENG&AwaitingReconsent=false",
    "bbLandingPage": "manage_profile",
    "_ga_TT5WXDW45Z": "GS2.1.s1752422464$o2$g1$t1752424880$j60$l0$h2009153933",
    "_uetsid": "05261c605fd011f08c250b5d96f3ec72",
    "_uetvid": "052630505fd011f0848e53c109253335",
    "_hjHasCachedUserAttributes": "true",
    "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjY3Mjc5MSIsImFwIjoiNTk0NDk5MDUwIiwiaWQiOiJjMThmNDEwZDZiY2U5ZGE0IiwidHIiOiIyY2ZhNTJlMzhkMGNmNjYwZjY2YmFlZDhhODdmMzUyZiIsInRpIjoxNzUyNDI0OTU3MTc4fX0="
}
URL = "https://boatbooker.com/manage/profile/request_phone_verification"
import time
def fetch(session, n):
    """Send one GET request."""
    try:
        response = session.get(URL, headers=headers, cookies=cookies, timeout=30)
        print(f"[{n}] {response.status_code}")
        try:
            print(response.json())
        except ValueError:
            # print(response.text)  # print trimmed response if not JSON
            pass
    except requests.RequestException as e:
        print(f"[{n}] ERROR: {e}")


def run_round(round_no):
    """Run 100 requests using one persistent session."""
    with requests.Session() as session:
        for i in range(1, 101):
            fetch(session, i)
    print(f"Round {round_no} completed\n")


if __name__ == "__main__":
    for i in range(1, 31):  # 30 rounds
        run_round(i)
        time.sleep(1)  # optional delay between rounds