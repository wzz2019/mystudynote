from seleniumcode.studypo.page.main_page import MainPage
from seleniumcode.studypo.page.contact_page import ContactPage
class TestAddMember():
    def test_add_member(self):
        main=MainPage()
        #在首页点击添加成员，跳转添加成员页面，填写信息，点保存，跳转到通讯录页面
        #找添加的人进行断言
        assert "xx" in
