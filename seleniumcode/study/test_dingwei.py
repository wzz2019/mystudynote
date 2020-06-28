from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class TestLocat():
    def setup_class(self):
        self.driver=Chrome()
        self.driver.implicitly_wait(3)

    def setup(self):
        self.driver.get("https://www.baidu.com")

    def teardown_class(self):
        self.driver.quit()

    def test_id(self):
        self.driver.find_element(By.ID,"kw").send_keys("百度")
        self.driver.find_element_by_id("su").click()
    def test_name(self):
        self.driver.find_element(By.NAME,"wd").send_keys("百度")
    def test_xpath(self):
        self.driver.find_element(By.XPATH,"//*[@name='wd']").send_keys("百度")
        self.driver.find_element_by_xpath("//*[@id='su']").click()
    def test_tag_name(self):
        # 输入框是input标签，按钮也是，所以这里也会报错
        self.driver.find_element(By.TAG_NAME,"input").send_keys("百度")
    def test_link(self):
        self.driver.find_element(By.LINK_TEXT,"新闻").click()
    def test_plink(self):
        self.driver.find_element_by_partial_link_text("闻").click()
    def test_classname(self):
        # 新闻链接，百度首页左上角的链接文字class name 都是相同的，所以此处会报错
        self.driver.find_element(By.CLASS_NAME,"mnav c-font-normal c-color-t").click()
    def test_cssselector(self):
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("百度")
        self.driver.find_element_by_css_selector("#su").click()