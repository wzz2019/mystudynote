from seleniumcode.studypo.page.main import Main

class TestRegister:
    def setup_class(self):
        self.main=Main()

    def teardown_class(self):
        self.main.exit()

    def test_register1(self):
       assert  self.main.goto_register().register()

    def test_register2(self):
       assert  self.main.goto_login().goto_register().register()
