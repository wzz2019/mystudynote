import pytest
import yaml
def func(x):
    return x + 1

@pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data_b.yml")))
def test_answer(a,b):
    assert func(a) == b
# a=yaml.safe_load(open("./data_b.yml"))
# print(a)
# print(type(a))

# #一组参数，变量是元组
# @pytest.mark.parametrize(('a','b'),[[1, 2], [2, 3], [6, 7]])
# def test_answer4(a,b):
#     assert func(a) == b

# #一组参数，变量是元组
# @pytest.mark.parametrize(('a','b'),[(1,2)])
# def test_answer4(a,b):
#     assert func(a) == b
#
# #多组参数，变量是string,值是列表，列表里面是元组
# @pytest.mark.parametrize('a,b',[(1,2),(2,4)])
# def test_answer2(a,b):
#     assert func(a) == b
#
# #多组参数，变量是列表
# @pytest.mark.parametrize(["a","b"],[(3,2),(3,4)])
# def test_answer3(a,b):
#     assert func(a) == b


