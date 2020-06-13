import allure
#标记功能模块
@allure.feature("登录功能")
class Test_Login():
    #标记用例名称
    @allure.story("登录成功")
    def test_login_success(self):
        print("登录的测试用例1：登录成功")

    @allure.story("登录失败")
    def test_login_failed(self):
        print("登录的测试用例2：登录失败")
        assert False
    #标记测试步骤
    @allure.story("用户名或密码输入")
    def test_login_fail(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录后登录失败了"):
            print("登录失败")
            assert False
