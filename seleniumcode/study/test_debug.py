from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class TestLogin:
    def test_debug_login(self):
        option=Options()
        option.debugger_address="127.0.0.1:9222"
        driver=webdriver.Chrome(options=option)

