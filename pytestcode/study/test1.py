# 模块级别 --对这个文件起作用，所有测试类之前执行
def setup_module():
    print("==>setup_module")
# 模块级别 --对这个文件起作用，所有测试类之后执行
def teardown_module():
    print("==>teardown_module")
#测试类1
class Test_a:
    #类级别开始--类里面所有方法之前执行
    def setup_class(self):
        print("==>setup_class1")
    #类级别结束--类里面所有方法之后执行
    def teardown_class(self):
        print("==>teardown_class1")
    #方法级开始--类里每个测试方法执行前执行
    def setup(self):
        print("-->setup_method1")
    #方法级结束--类里每个测试方法执行后执行
    def teardown(self):
        print("-->teardown_method1")
    def test_a(self):
        print("-》》test_a1")
    def test_b(self):
        print("-》》test_b1")
        assert 0
#测试类2
class Test_b:
    #类级别开始--类里面所有方法之前执行
    def setup_class(self):
        print("==>setup_class2")
    #类级别结束--类里面所有方法之后执行
    def teardown_class(self):
        print("==>teardown_class2")
    #方法级开始--类里每个测试方法执行前执行
    def setup(self):
        print("-->setup_method2")
    #方法级结束--类里每个测试方法执行后执行
    def teardown(self):
        print("-->teardown_method2")
    def test_a(self):
        print("-》》test_a2")
        assert 0
    def test_b(self):
        print("-》》test_b2")
