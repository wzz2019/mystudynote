# conftest.py
import pytest

@pytest.fixture(scope="class")
def cal_fixture():
    print("开始计算")
    yield
    print("结束计算")