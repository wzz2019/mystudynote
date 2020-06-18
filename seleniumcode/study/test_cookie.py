from selenium import webdriver
import time,json
class Test_a():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(375,667)
        self.driver.get("https://huzhu6.qschou.com/")
        time.sleep(5)

    def teardown(self):
        self.driver.quit()

    # def test_1(self):
    #     self.driver.get("https://huzhu6.qschou.com/")
    #     time.sleep(35)
    #     cookies=self.driver.get_cookies()
    #     with open("cookie.json","w") as f:
    #         json.dump(cookies,f)

    # def test_1(self):
    #     self.driver.get("https://huzhu6.qschou.com/")

    def test_cookie_login(self):
        cookies=json.load(open("cookie.json"))
        for cookie in cookies:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])

            if cookie["name"]=="Passport-Token-All":
                self.driver.add_cookie(cookie)
                break
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)

