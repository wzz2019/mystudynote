import json

from selenium.webdriver.common.by import By
from seleniumcode.studypo.page.base_page import BasePage
from seleniumcode.studypo.page.register import Register

'''企业微信扫码登录页面'''
class Login(BasePage):
    # 页面元素定位
    # 企业注册的链接
    __link_register=(By.LINK_TEXT,"企业注册")


    def goto_register(self):
        '''
        describ:点击页面的企业注册链接，进入注册页面
        :return:
        '''
        self.find(*self.__link_register).click()
        return Register(self._driver)

    def save_cookies(self):
        cookies = self._driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)
