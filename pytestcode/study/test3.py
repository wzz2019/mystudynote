import pytest

#使用如下固定语法，可以每个测试方法都调用fixture33
pytestmark=pytest.mark.usefixtures("fixture33")

#class及function级别的fixture加到最上面即可
@pytest.mark.usefixtures("fixture1")
@pytest.mark.usefixtures("fixture2")

#同一个级别的fixture按从下到上的顺序执行
@pytest.mark.usefixtures("fixture31")
@pytest.mark.usefixtures("fixture32")

class Test_f1:
    # 测试方法中直接引用fixture函数
    def test_f1a1(self,fixture4):
        print("《1-1》test_f1a1 in class Test_f1")
    def test_f1a2(self):
        print("《1-2》test_f1a2 in class Test_f1")

#如果类前面不加usefixtures装饰器的话，是不会执行class及function级别的fixture
class Test_f2:
    def test_f2a1(self):
        print("《2-1》test_f2a1 in  class Test_f2")
    def test_f2a2(self):
        print("《2-2》test_f2a2 in  class Test_f2")
