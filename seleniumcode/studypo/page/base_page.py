from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#BasePage的定义的：它是一个其他page的公共方法的封装，它是一个底层使用的框架
# 因此不能耦合业务相关的东西，如get的url
class BasePage():
    _base_url = ""
    def __init__(self,driver_init=None):
        if driver_init==None:
            #复用已经打开的浏览器，需要关闭所有浏览器再启动
            #Windows启动方式： chrome --remote-debugging-port=9222
            option=Options()
            option.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=option)
            # self.driver=webdriver.chrome()
        else:
            self.driver=driver_init

        if self._base_url != "":
            self.driver.get(self._base_url)