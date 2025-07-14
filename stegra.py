import requests

url = "https://stegra.talent-community.com/v1/api/freelancer/resetPhoneCode"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Origin": "https://stegra.talent-community.com",
    "Referer": "https://stegra.talent-community.com/app/mobile-activation/38641634750",
    "Cookie": (
        "auth.strategy=local; i18n_redirected=en; _gcl_au=1.1.1089240026.1752400999; "
        "_ga=GA1.1.1665368361.1752400999; ajs_user_id=null; ajs_group_id=null; "
        'ajs_anonymous_id="%2291a10f18-ae41-45ef-8fcd-062324f9f451%22"; '
        "OptanonAlertBoxClosed=2025-07-13T10:03:19.710Z; "
        "_hjSession_3216004=eyJpZCI6IjYxYTJjNGQxLWE1ZmYtNDVlNS1hNjNiLTRhOGQxYjY5YzJiMCIsImMiOjE3NTI0MDA5OTk4NzYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; "
        "kampyle_userid=1e86-22d3-cf4a-b717-1d8e-e43b-5df2-ba91; "
        "auth._brws_id=686347dc-891b-4909-9351-da49631d90e9; "
        "_hjSessionUser_3216004=eyJpZCI6IjFhZjZhNDYxLWM1NjYtNWI4Ny04NDE5LTIzZmEyZjI4NzQ5NiIsImNyZWF0ZWQiOjE3NTI0MDA5OTk4NzUsImV4aXN0aW5nIjp0cnVlfQ==; "
        "OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jul+13+2025+13%3A04%3A08+GMT%2B0300+(Eastern+European+Summer+Time)&version=202505.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=79d4a512-85d6-4b86-994b-4aef1cb2ef9c&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0001%3A1&intType=3&geolocation=%3B&AwaitingReconsent=false; "
        "kampyleUserSession=1752401049273; kampyleUserSessionsCount=27; "
        "kampyleUserPercentile=29.79711430965535; kampyleSessionPageCounter=1; "
        "da_sid=9C0C616C8E33AE80E281AA13AC554DAF05.0|4|0|3; "
        "da_lid=8A6D55D09A7CEA50E889BB99E1FC10DE92|0|0|0; "
        "da_intState=0; _ga_QQ0W51J18E=GS2.1.s1752400999$o1$g1$t1752401353$j60$l0$h901925004; "
        "_dd_s=aid=907b36e9-86ef-4113-8dcd-01aff377c5bd&rum=1&id=29ac4528-11da-40ca-9873-824df2720f3c&created=1752400243651&expire=1752402317976"
    )
}

payload = {
    "mobileCode": "386",
    "mobileNumber": "41634750",
    "reCaptchaToken": "03AFcWeA6hehKul003BjRLzfpo5UfQd96Xzf_KaQnAGJk9CA8_cqxvjpPLriV0huzqa9FeCER0-xTzN94gr-qayD9X7g1UHTrpRNhhi8lTAECYwBeT33eZP-6v9huu-uejtOL4pSphNtw-y_NcOp2W4quzFNpGqFCtwrCmVUMelvMvrtVYOC-kGhBk6ziX-hqUo84WOJmPP_ARrK-w4tcqXsAjkmUHzYZf4KY63ITS2K2Y9OqDUCmyOeLG7klaLV8jT7dYqVd9rls5Sq3cCie58BeXFavfRaluz5MkMJvFip0RmSeWQOsHcAdkOIYlx7izP9rczYTRGRsRIrXz94D91cgxnHG9kTfF5j5YCcSiYpEf6m_M_BY2_uuClWgoezxLjsapbRjhEYCqBwo_Qgomp52XM8lso_Hpa8QXtXT72q4UPFGiFVvRixinVlMrusZgCpFoCcVhdXUY-osLmqGWCExpj0RKiJezv9oVMDNMi-UuNrWAQ44HN12nM0IWZ1niAvgJ1zVsJU2xfNuqRj7qgMd27C5MwsZr-8vMl_-7a9s8pU_Ze3eX_FqrsgF6gNyY7gD3mTbmPyNGRlh-hGjmwOai26EwFbLQe8eFB2CjVT2q_wnH8kc8L_tCsznoFnOzYW03qa9t1TfTrodfe697IVT6kGBvRvW4VmQ1bWiFB5QjA5KFzrRqT3Bwl7tcbBmN8qrERpJrSqrtBB-qetUvzmFI2T5EmaEiQ0eRh6W5nvThQwrj3Euj9B7nfmcmXodL-1Vsl4X8n1KgxeYlDWV4aSwkKTfZELnYtQyQP1v3fIZoKsran4vjvRA6IPY9fxn4Vg5DM49hxDGo-ZkM7YEdj_zqzhaJzvDyH55wx7btxokbKQm8VbDUeGaGONWtjgbMVdWMJ3HQeUvwkMe_UL75gojZT3Kc7kGr-KQUzfTzKv8cmBJtwh2lIpTv1nOgWrobDYOAmJkkvb2x"
}

response = requests.put(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
