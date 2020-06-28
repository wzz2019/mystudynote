from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from do_wait import WaitUntilFind

class TestDebug:
    def setup_class(self):
        # 调试模式打开浏览器
        # chrome - -remote - debugging - port = 9222

        #复用调试模式打开的浏览器
        option=Options()
        option.debugger_address="localhost:9222"
        self.driver=webdriver.Chrome(options=option)
        # self.driver.implicitly_wait(5) #隐式等待
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        #调用显示等待的封装类
        self.wait=WaitUntilFind(self.driver)

    def test_open_contacts(self):
        # 直接传定位元组
        self.wait.find_element_e(*(By.ID,"menu_contacts")).click()
    def test_open_apps(self):
        #定义定位元组
        locat_apps=(By.ID,"menu_apps")
        self.wait.find_element_e(*locat_apps).click()
    def test_open_tools(self):
        locat_tools=(By.ID,"menu_manageTools")
        self.wait.find_element_f(*locat_tools).click()
    def test_open_apps2(self):
        #自行封装
        locat_apps=(By.ID,"menu_apps")
        self.wait.find_element_g(*locat_apps).click()