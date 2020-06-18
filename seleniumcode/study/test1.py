from selenium  import  webdriver
import time
class Test_a():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_1(self):
        self.driver.get("https://testerhome.com/")
        # time.sleep(2)
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/a').click()
