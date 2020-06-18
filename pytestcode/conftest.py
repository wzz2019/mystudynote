# conftest.py
import pytest

#session级别
@pytest.fixture(scope="session")
def fixture1():
    print("【1-1】session setup")
    # 使用yield，前面实现的是setup方法，后面实现的teardown方法
    yield
    print("【1-2】session teardown")
#module级别
@pytest.fixture(scope="module")
def fixture2():
    print("【2-1】module setup")
    yield
    print("【2-2】module teardown")
#class级别
@pytest.fixture(scope="class")
def fixture32():
    print("【32-1】class setup")
    yield
    print("【32-2】class teardown")
#class级别
@pytest.fixture(scope="class")
def fixture31():
    print("【31-1】class setup")
    yield
    print("【31-2】class teardown")
#class级别
@pytest.fixture(scope="class")
def fixture33():
    print("【33-1】class setup")
    yield
    print("【33-2】class teardown")
#function级别
@pytest.fixture(scope="function")
def fixture4():
    print("【4-1】function setup")
    yield fixture4
    print("【4-2】function teardown")

#使用参数autouse="true"，那么就可以在py文件中执行时自动调用，无需手动引用
@pytest.fixture(scope="function",autouse="true")
def fixture5():
    print("【5-1】function setup")
    yield
    print("【5-2】function teardown")