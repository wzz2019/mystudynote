import allure
@allure.feature("报告中附加信息")
class Test_attach():
    def test_attach_text1(self):
        allure.attach("这是一个纯文本",
                      attachment_type=allure.attachment_type.TEXT)

    def test_attach_text2(self):
        allure.attach(body="文本文本文本文本文本文本文本",
                      name="这是一个纯文本",
                      attachment_type=allure.attachment_type.TEXT)

    def test_attach_html(self):
        allure.attach(body='''
                        <body>
                        <h>正文</h>
                        <p>正文</p>
                        </body>
                        ''',
                      name="这是一个Html",
                      attachment_type=allure.attachment_type.HTML)

    def test_attach_photo(self):
        allure.attach.file(source="../files/pic1.jpg",
                      name="这是一个图片",
                      attachment_type=allure.attachment_type.HTML)