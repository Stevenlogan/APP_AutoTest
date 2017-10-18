#coding:utf-8

from appium import webdriver


class OpenApp():

    def __init__(self,devicename):
        self.d_caps = {
    'platformName':'Android',
    'platformVersion':'6.0',
    'deviceName':devicename,
    'appPackage':'com.coomix.app.car',
    'appActivity':'com.coomix.app.car.activity.BootActivity'
    }

    def open_app(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.d_caps)
        return driver