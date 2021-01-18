import pytest

#pytest.ini文件中不能有中文注释？
#注册一个命令行选项
def pytest_addoption(parser):
    mygroup=parser.getgroup("mydiytool")
    mygroup.addoption(
        "--env",
        default='test',
        dest='env',
        help='set run env'
    )

#读取命令行选项的值
@pytest.fixture(scope="session",autouse="true")
def env(request):
    return request.config.getoption("--env",default="test")

#引用命令行选项的值
@pytest.fixture(scope="session",autouse="true")
def env_fixture(env):
    if env=="test":
        print("test env")
    else:  print(f"{env}  env")
    assert 1
