
import time,json

cookies = json.load(open("cookie.json"))
for cookie in cookies:
    if cookie["name"] == "Passport-Token-All":
        print(cookie)
        break