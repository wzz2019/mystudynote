
from selenium.webdriver.common.by import By

from seleniumcode.studypo.page.add_member_page import AddMember
from seleniumcode.studypo.page.base_page import BasePage

# 企业微信首页
class MainPage(BasePage):
    __base_url = "https://work.weixin.qq.com"

    def goto_add_member(self):
        #跳转，函数名可命名为goto**
        #点击添加成员按钮
        self.driver.find_element(By.LINK_TEXT,"添加成员" )

        return  AddMember(self.driver)
