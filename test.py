import requests

url = "https://auth.ticketmaster.com/verify-otp/json/send/otp/sms?clientToken=eyJhbGciOiJka...<truncated for brevity>...g54"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-us",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://auth.ticketmaster.com",
    "Referer": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=mytmlogin&hideLeftPanel=false&integratorId=prd1741.iccp&intSiteToken=tm-us&TMUO=west_55UHUsKTiSvu4AxT2nb+epckIC0lh/7abNUQu5rQjzU=&deviceId=wUaboSf7QsXHycbKw8TKx73GvcY6XPNX1AReMw&doNotTrack=false&disableAutoOptIn=false",
    "tm-client-id": "baf9f4135217.web.ticketmaster.us",
    "tm-integrator-id": "prd1741.iccp",
    "tm-placement-id": "mytmlogin",
    "tm-site-token": "tm-us",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0"
}

cookies = {
    "TMAUO": "west_WOTpvH9HmXomTp1i00d0k6cLjJ+Tuq2Q7mKAb0cNjSo=",
    "ma.LANGUAGE": "en-us",
    "ma.SID": "vCITuYUlqzn-Jg3HzJmMX90T3QbKJTqkzu0xCSCXryjVRvbvLimWyM5zoFL54ZN2jeAV4YzK2RkErW9E9daO",
    "ma.BID": "vCdBSvi4Jjaa-uVgMMOnhAEO5J4r5KCwC-_mbP-2ytj3XYtIMVgjH1M7V5RnDz_1LZfbX4HKyu30z_o",
    "eps_sid": "352b71341aceeb363bc0d3d81a3055c00d4b3d18",
    # Add any additional cookies you need from the browser here
}

# Your full payload as Python dictionary
payload = {
    "emailAddress": None,
    "phoneNumber": "+221766415529",
    "userIdentifier": "cOFkILwXHpyawFLjqoNom8KK_d9xKyP0O0L5ymlDxQH9pZhLd6g-yG8tfIuNQr-EtYi9O1sBU-JS_DnqR63I-CR5JztZO1pmP8LvI7WEJQKD9VPENddvSsUzpZfJHcE_Pxl9ZtIUy9UkFZyw_t_HT5F2uc6r1MIpQswPla5YqJ7_GG673yRpei4neOGGjwria2Jq6GIynTIS4nQTVt5UC0GLQPqbwl7mfTU1u3Ugi5yY2FkUs347Ng_cUFLc8aU8SYIPih_Q2HhO50cOLY2z6eFU-QTq8Y_kWOdyXava2il0rOfhJI8fQFZ9-yIY084IXTM7TH1JyHPIYHcZIQGTRRhk480wdunRyDkPce5Y41wn-AcVL9JkjUtWGSiHlSfku7xbiYRwM9QaWTe4412C-pdD6R4L062310NsDjNsBazJXMDTZhghBoGb4FJ77s9pmjw0NaLIC_uCbEPpY8w0dwODoRrAwMuPmD4eYjLMGkbJKMVR6VjwvhXOWWlYcF5l9rr8HPykr9LSUq7cFUYuwwyAMYLFsLElqZvWlin5iiy1IHjzHKPWqsPjbi4oTfN9rBFCr-8GUb08rPXzYlMtkwkvNXZbxDzxEEQVMkn7Rx1GXOe83sXlBC1nvEZZpdJwrvvzlXPqRSUtApHUIaCR7E9dx7PNHOJ9IkyS7M0Kn4uQCpNM1FqAVfL5HqISk_b2_dp-EEZnJ_WC-ZE3fyAv8KBamMfskIGsUSS412G00KGhoKG15VS2ELCgOlc_63Q6rhygmZ-RhyhjIwqS6Y34mxKVtC0Q8hq0DReHQKVDLlq4cjsfXNVGNS4Tz2Ogg7fw1Kvge_4RIjOFrHJ_S9cpVS6Pm_sFaBi1sDesWYg9uAMvJLiwbSHquLVFSc_nDIedWewu8O0tzhqDkfbS6dFAUg",
    "flow": "bind_phone",
    "referenceId": "cOFkILwXHpyawFLjqoNom8KK_d9xKyP0O0L5ymlDxQH9pZhLd6g-yG8tfIuNQr-EtYi9O1sBU-JS_DnqR63I-CR5JztZO1pmP8LvI7WEJQKD9VPENddvSsUzpZfJHcE_Pxl9ZtIUy9UkFZyw_t_HT5F2uc6r1MIpQswPla5YqJ7_GG673yRpei4neOGGjwria2Jq6GIynTIS4nQTVt5UC0GLQPqbwl7mfTU1u3Ugi5yY2FkUs347Ng_cUFLc8aU8SYIPih_Q2HhO50cOLY2z6eFU-QTq8Y_kWOdyXava2il0rOfhJI8fQFZ9-yIY084IXTM7TH1JyHPIYHcZIQGTRRhk480wdunRyDkPce5Y41wn-AcVL9JkjUtWGSiHlSfku7xbiYRwM9QaWTe4412C-pdD6R4L062310NsDjNsBazJXMDTZhghBoGb4FJ77s9pmjw0NaLIC_uCbEPpY8w0dwODoRrAwMuPmD4eYjLMGkbJKMVR6VjwvhXOWWlYcF5l9rr8HPykr9LSUq7cFUYuwwyAMYLFsLElqZvWlin5iiy1IHjzHKPWqsPjbi4oTfN9rBFCr-8GUb08rPXzYlMtkwkvNXZbxDzxEEQVMkn7Rx1GXOe83sXlBC1nvEZZpdJwrvvzlXPqRSUtApHUIaCR7E9dx7PNHOJ9IkyS7M0Kn4uQCpNM1FqAVfL5HqISk_b2_dp-EEZnJ_WC-ZE3fyAv8KBamMfskIGsUSS412G00KGhoKG15VS2ELCgOlc_63Q6rhygmZ-RhyhjIwqS6Y34mxKVtC0Q8hq0DReHQKVDLlq4cjsfXNVGNS4Tz2Ogg7fw1Kvge_4RIjOFrHJ_S9cpVS6Pm_sFaBi1sDesWYg9uAMvJLiwbSHquLVFSc_nDIedWewu8O0tzhqDkfbS6dFAUg"
}

# Send the POST request
response = requests.post(url, headers=headers, cookies=cookies, json=payload)

# Print status and response
print("Status:", response.status_code)
print("Response body:", response.text)
