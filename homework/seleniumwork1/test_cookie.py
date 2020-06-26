from selenium import webdriver
import time,json
from selenium.webdriver.common.by import By


class Test_cookie():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown(self):
        self.driver.quit()

    def test_cookie_login(self):
        cookies=json.load(open("cookie.json"))
        for cookie in cookies:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            self.driver.add_cookie(cookie)
        time.sleep(5)
        self.driver.refresh()
        assert self.driver.find_element(By.ID, "menu_contacts")
