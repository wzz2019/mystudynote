import pytest
import json
from time import sleep
from selenium import webdriver

from seleniumcode.studypo.page.main import Main

@pytest.fixture(scope="session")
def savecookies():
    loginpage = Main().goto_login()
    sleep(15)
    loginpage.save_cookies()
