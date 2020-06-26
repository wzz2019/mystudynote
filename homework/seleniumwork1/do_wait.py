
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class WaitUntilFind:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        # self.by=by
        # self.value=value


    def find_element_f(self,*loc):
        '''
        显示等待：实现方式1：WebDriverWait + until 通过find_element的is_displayed()等方法判断
        :param loc:参数传入定位元组
        :return:
        '''
        try:
            WebDriverWait(self.driver,10).until(lambda the_driver: the_driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("未找到元素")

    def find_element_e(self,*loc):
        '''
        显示等待：实现方式2：WebDriverWait + until结合expected_conditions模块的判断方法实现
        :param loc:参数传入带*的定位元组
        :return:
        '''
        try:
            self.wait.until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("未找到元素")