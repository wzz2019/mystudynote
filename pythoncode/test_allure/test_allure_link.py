import allure
#关联链接
@allure.feature("关联链接")
class Test_link():
    #链接
    @allure.link("https://www.baidu.com")
    def test_login_link1(self):
        print("这是跳转链接")
    #链接
    @allure.link("https://www.baidu.com",name="链接")
    def test_login_link2(self):
        print("这是跳转链接只显示名称")

    TEST_LINK="https://www.baidu.com"
    @allure.testcase(TEST_LINK,"登录用例")
    def test_login_testcase_link(self):
        print("这是登录用例地址")

    BUG_LINK="https://www.baidu.com?issue_id="
    @allure.issue(BUG_LINK+'140',"这是一个issue")
    def test_login_issue_link(self):
        print("这是一个issue地址")
