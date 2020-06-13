import allure

@allure.feature("测试级别")
class Test_level():

    @allure.severity(allure.severity_level.BLOCKER)
    def test_a(self):
        print("这是blocker级别")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_b(self):
        print("这是critical级别")
    @allure.severity(allure.severity_level.NORMAL)
    def test_c(self):
        print("这是normal级别")
    @allure.severity(allure.severity_level.MINOR)
    def test_d(self):
        print("这是minor级别")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_e(self):
        print("这是trivial级别")