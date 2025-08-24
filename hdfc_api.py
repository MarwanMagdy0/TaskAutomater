import requests

url = "https://osappsext.hdfc.com/spotoffer_fe/screenservices/SPOTOFFER_FE/BasicInformation_WebBlocks/BasicInformation_Step1/ActionReCAPTCHA_ValidateAndProceed"

headers = {
    ":authority": "osappsext.hdfc.com",
    ":method": "POST",
    ":path": "/spotoffer_fe/screenservices/SPOTOFFER_FE/BasicInformation_WebBlocks/BasicInformation_Step1/ActionReCAPTCHA_ValidateAndProceed",
    ":scheme": "https",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
    "content-length": "2063",
    "content-type": "application/json; charset=UTF-8",
    "origin": "https://osappsext.hdfc.com",
    "priority": "u=1, i",
    "referer": "https://osappsext.hdfc.com/spotoffer_fe/BasicInformation",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"138.0.7204.100\"",
    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"138.0.7204.100\", \"Google Chrome\";v=\"138.0.7204.100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-ch-ua-platform-version": "\"5.15.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-csrftoken": "T6C+9iB49TLra4jEsMeSckDMNhQ=",
}

cookies = {
    "osVisitor": "7823a517-2729-4443-af74-52a681fa76b7",
    "nr1Users": "lid=Anonymous;tuu=0;exp=0;rhs=XBC1ss1nOgYW1SmqUjSxLucVOAg=;hmc=WhLHxtPaFripVsdOy/cZHHaHEyc=",
    "nr2Users": "crf=T6C+9iB49TLra4jEsMeSckDMNhQ=;uid=0;unm=",
    "_gcl_au": "1.1.502595058.1755187594",
    "cf_clearance": "N7Db82q9hOje2gwysSc_DLuy6LZ.qBPjSdceH.9_oTs-1755614976-1.2.1.1-4dOyl1BLiZGDnO_mpJ9Jua2OL_Ix2lYXrcFhPRuR0gPX8Pq84nyjU41wRwniDXkHbWO4ZXfKSsJqkppWN2rewW6nSPlU1_zC5U84tJAdmSXTIbsmAtTzlfpF3X8gfsUse5GYzPt.xGNXgyitjvTweHiu63bwABuwS2mBZoi2Sx7kx42ApAEvHeQpldgcWDr44xDO6K_mijgdcDCvAnpK34l.mO65CLM7oL.IRZEGuXY",
    "_cfuvid": "8XelGH8Dd6Qrby1ecN89XOwCOEtPwsATxy0yfBdWY78-1755614977612-0.0.1.1-604800000",
    "ASP.NET_SessionId": "wxnyzrob0phvmyrxeunvil10",
    "at_check": "true",
    "_clck": "1yngdxi^2^fyl^0^2052",
    "AMCVS_442A49D760E2A8340A495C48@AdobeOrg": "1",
    "AMCV_442A49D760E2A8340A495C48@AdobeOrg": "1176715910|MCIDTS|20319|MCMID|62751964335176487773140967175031634722|MCAAMLH-1756221052|6|MCAAMB-1756221052|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1755623452s|NONE|MCSYNCSOP|411-20322|vVersion|5.4.0",
    "s_cc": "true",
    "mbox": "PC#3eed4b7c176549a1b9cb06d8904d688f.34_0#1818864213|session#428da38cfef9437390bf03fd40dc24fc#1755621273",
    "_uetsid": "7a861b407b9b11f0b7311bf4257e88d9",
    "_uetvid": "21599160747811f0a432f95117049199",
    "s_nr365": "1755619415331-Repeat",
    "_clsk": "102m1u0^1755626633293^1^1^b.clarity.ms/collect",
    "__cf_bm": "ijSol3HPBqG4lFZP6TDkMZWdhEDk6MZzL7E9CfGZ450-1755626634-1.0.1.1-LFyiVOeAKF2ghydAt2OeCDMY2Wr_C01F4EoQwXi1THZs.mkZrnfF07r_F5s5rthASgiDhekYHYQd7HrADkNJWqQo3RZQBGbEiImI7wNewQQ",
    "osVisit": "65a8acf8-0b94-4949-b994-deedafc367f3"
}

payload = {
    "versionInfo": {
        "moduleVersion": "vQVTsBkYAcpp5z1aWOOhvQ",
        "apiVersion": "YOgu9+U9gncdtOjrfgzkgg"
    },
    "viewName": "MainFlow.BasicInformation",
    "inputParameters": {
        "MobileNumber": "258823460497",
        "RequestNumber": "1",
        "ValidateOTPTimeStamp": "19-Aug-2025 09:10 PM",
        "IsSendOTPForMobileCL": False,
        "Token": "0cAFcWeA4WA6MgztbLHnfhCo0vMIdGqlcWjpI7CteqrUfQqQ-8lXJbAXQWLZNyOZlBDt5QHNMtIiepywC6cIcoVQQyUaxw_dfkAstquurVQAbXLbwBos7zwxw_eeKp36SamJfrE2jofLCDgjNdLEFr6Pursc4wGp-_sHfsmmf9uuACqjUk0fw-FyeDnWmPh0PRLg3fnXmYXwiA5S23ci4oiDE_WIF77b1y9dxiLa4tyvDyJeKJR6pS2fh5cfZXnmYTZBROtfoSDbpt2jRiNgkoDJQNvx9rkRiTvNjy8W_6nZKp0VjvP5ArNhwPFkSmu7jNgmit3j1e65vfMIktVti_d-AZya0gO8RaYSG4pR6KzzpCu2Fs9kvoakEhKp80aSJxpAWb9rI_tQjtnhAX5G1L_6gRkY7ursEeysvyV-BU6w97iiGrLA6F7lxE6_eKlYZGLzx7LsvQplg7TU7dQff4RN6mBA7eemN2IDeZOigmaGjaa5sjKMpEOhM7SCFQy3gV_W5dlDSjZrlOflHZlTvtB7YPttGk0_tgxJoabjNsI61TvesY8gj78vbKWY6hVaCjl5xNj_uGmhN5lyXSe81ImciRUtySkw07aYYiyAIC7_5RRMGMBKmOKpda3MxhKuBtnkMRHVEMiWulNHcHJqhpFNp_57nvxu3P_R9kOLu_SPFkycXpaFeMWpnf3y7HZXm10CsJddKh-aqJh64_iSFeemkmODrDw5_wtj-g1cMllwrYuRHK80QMj6qTbaXVt9bd0FmrJQPCcstq6NOCfTO4DMwFyg5EKph6Xfr6zRbXNZJeRh1DRx0oCykN544Bw6NusSAG3up0oTuL__1XKKqyaD60HHWeZ6lZ8Id0_iTcjbpemu0UElUhGm3vVrAKZAKj3YFo8GU0BW8qeNUX0qMHyIjcQgRSk7FwnM_ToKhCUmIscO2wqVTjV8bDjqnrTTdBW9_d-ImTxPhaQpire-H8D_tdVhPBrztv8MX7Du0J8H2G2GHFIeXcaUHuczdG0gtY_FdwLWS27gMUOPvM5rFY1ZEKJraeH3wy6IPYlK5G7-QJZC6o8SEH6t2JKRvyj7MbrpGvKeMYY2XLnyKwJBQMe8svHrdHplTgSjOgKhdUsF5bDoWB4jIXyqny4DvsPpD4rp_vv2w0h4ou0xJOYFBY2MXDai7LNI61URUeJCzwk7ZHWH6rdTveaJjBDdAUf8h_BCJe_siXk5GcA1VZMeRfmOZeuU8_2bKcsYWfAxzG7M0p281ixReKiY6nzu0W8bOZbEAYDGmoE-05YLbNIt8Jk_qbLHRtDdNjEoXGemAKn7NWrKcmnd4kRzMBYROfx2U5YV5u2Jp_2Dn_vGq_vwZKUpevewmHDQpe-gZQ3WlUJ9yMhYJaQ1VntOTuAsTak6mg8aVQukuLTiLFCPg2pfsYQKBQxqGQxEMf5aDUZKFMPovNRnhBPxJoJcTWG_sROftRS7iB5sMpQ9f2bWADyvUAD1XBie5NRSvTEiZhG8khzEJIHeieR7LuiYnjr8JDi506wRvTVYVUJACTxmuEkSkiSNM-OG29oCZT7N3zS0P-3c9dGHQTq-ZGNHufieZ9ll9YnCyexFg9m0t6SPOAzdMglSELCXpY6kxOlc0x3MK2tZlRoU4JoVZl-no",
        "EmailID": "",
        "ValidMinutes": 0,
        "ValidTillOTPTimeStamp": "",
        "IsSendOTPForEmailCL": False,
        "ExpectedAction": "NRI/Mobile"
    }
}

response = requests.post(url, headers=headers, cookies=cookies, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)
