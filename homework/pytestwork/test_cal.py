import yaml
import pytest
import allure
from cal import Calculator

@allure.feature("测试计算器")
@pytest.mark.usefixtures("test_fixture")
@pytest.mark.usefixtures("cal_fixture")
class TestA:
    @allure.story("加法")
    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_add.yml"))["add"]
                             )
    def test_add(self,a,b,c):
        cal=Calculator()
        assert c==cal.add(a,b)

    @allure.story("减法")
    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_sub.yml"))["sub"]
                             )
    def test_sub(self,a,b,c):
        cal=Calculator()
        assert c==cal.sub(a,b)


    @allure.story("乘法")
    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_mul.yml"))["mul"]
                             )
    def test_mul(self,a,b,c):
        cal=Calculator()
        assert c==cal.mul(a,b)


    @allure.story("除法")
    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_div.yml"))["div"]
                             )
    def test_div(self,a,b,c):
        cal=Calculator()
        assert c==cal.div(a,b)


