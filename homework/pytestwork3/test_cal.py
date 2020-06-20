import yaml
import pytest
import allure
from cal import Calculator

@allure.story("加法")
#定义执行顺序
@pytest.mark.run(order=1)
#定义依赖
@pytest.mark.dependency(name="add")
@pytest.mark.parametrize(["a", "b","c"],yaml.safe_load(open("./data_cal_add.yml"))["add"])
def test_add(a,b,c):
    cal=Calculator()
    assert c==cal.add(a,b)


@allure.story("乘法")
@pytest.mark.run(order=3)
@pytest.mark.dependency(name="mul")
@pytest.mark.parametrize(["a", "b","c"],yaml.safe_load(open("./data_cal_mul.yml"))["mul"])
def test_mul(a,b,c):
    cal=Calculator()
    assert c==cal.mul(a,b)

@allure.story("减法")
@pytest.mark.run(order=2)
#设定依赖关系
@pytest.mark.dependency(name="sub",depends=["add"])
@pytest.mark.parametrize(["a", "b","c"],yaml.safe_load(open("./data_cal_sub.yml"))["sub"])
def check_sub(a,b,c):
    cal=Calculator()
    assert c==cal.sub(a,b)

@allure.story("除法")
@pytest.mark.run(order=4)
@pytest.mark.dependency(name="div",depends=["mul"])
@pytest.mark.parametrize(["a", "b","c"],yaml.safe_load(open("./data_cal_div.yml"))["div"])
def check_div(a,b,c):
    cal=Calculator()
    assert c==cal.div(a,b)
