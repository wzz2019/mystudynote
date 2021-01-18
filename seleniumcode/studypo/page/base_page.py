from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# ==========封装BasePage======================
#   BasePage的定义：
#       它是一个其他page的公共方法的封装
#       它是一个底层使用的框架
#       因此不能耦合业务相关的东西，如get的url
# ============================================

class BasePage():
    # 定义url
    _base_url = ""
    # 初始化driver
    def __init__(self,driver:WebDriver=None):

        # 判断driver是否已经初始化，否则先初始化，是则传递driver
        if driver is None:
            self._driver = webdriver.Chrome()

            # #复用已经打开的浏览器，需要关闭所有浏览器再启动
            # #Windows启动方式： chrome --remote-debugging-port=9222
            # option=Options()
            # option.debugger_address="127.0.0.1:9222"
            # self.driver=webdriver.Chrome(options=option)
        else:
            self._driver=driver

        #打开url
        if self._base_url != "":
            self._driver.get(self._base_url)

        #定义显式等待时间
        self.__wait=WebDriverWait(self._driver,10)

    # 封装显式等待查找单一元素
    def find(self,*loc):
        '''
        显示等待：WebDriverWait + until结合expected_conditions模块的判断方法实现
        :param loc:参数传入带*的定位元组
        :return:element对象
        '''
        try:
            self.__wait.until(EC.visibility_of_element_located(loc))
            return self._driver.find_element(*loc)
        except:
            print("未找到元素")
    #封装滑动页面查找单一元素
    def scolltofind(self,*loc):


    def exit(self):
        self._driver.quit()