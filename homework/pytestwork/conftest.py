# conftest.py
import pytest

@pytest.fixture(scope="class")
def test_fixture():
    print("开始测试")
    yield
    print("结束测试")

@pytest.fixture(scope="function")
def cal_fixture():
    print("开始计算")
    yield
    print("结束计算")