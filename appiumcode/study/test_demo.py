import appium
from appium import webdriver

desire_cap={}
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',desire_cap)
