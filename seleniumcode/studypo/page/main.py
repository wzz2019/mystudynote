from selenium.webdriver.common.by import By

from seleniumcode.studypo.page.base_page import BasePage
from seleniumcode.studypo.page.login import Login
from seleniumcode.studypo.page.register import Register

'''这是企业微信主页'''
class Main(BasePage):
    _base_url ="https://work.weixin.qq.com/"
    # 这里集中定义元素定位
    '''立即注册按钮'''
    __button_register =(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn")
    '''企业登录按钮'''
    __button_login =(By.CSS_SELECTOR,".index_top_operation_loginBtn")

    def goto_register(self):
        self.find(*self.__button_register).click()
        return Register(self._driver)


    def goto_login(self):
        self.find(*self.__button_login).click()
        return Login(self._driver)