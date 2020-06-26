import json

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_savecookie():
    #复用调试模式打开的浏览器
    option=Options()
    option.debugger_address="localhost:9222"
    driver=webdriver.Chrome(options=option)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")

    cookies=driver.get_cookies()
    with open("cookie.json","w") as f:
        json.dump(cookies,f)