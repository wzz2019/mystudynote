from selenium.webdriver.common.by import By

from seleniumcode.studypo.page.base_page import BasePage


class Register(BasePage):
    __input_name=(By.ID,"corp_name")
    __button_zhuce=(By.ID,".submit_btn")
    __checkbox_agree=(By.CSS_SELECTOR,".iagree")
    def register(self):
        self.find(*self.__input_name).send_keys("zhuce")
        self.find(*self.__checkbox_agree).click()
        self.find(*self.__button_zhuce).click()
        return True
