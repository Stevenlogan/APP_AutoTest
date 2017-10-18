#coding:utf8


import os
import unittest
from OpenApp import *
import sys
reload(sys)
sys.setdefaultencoding('gbk')
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


class Test(unittest.TestCase):
    def setUp(self):
        self.device_name = raw_input('Enter your devicename:')
        openapp = OpenApp(self.device_name)
        self.driver = openapp.open_app()
        print u'测试开始'
        self.driver.implicitly_wait(10)  # 全局等待10s
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_mine").click()  # 点击进入“我的”界面
        self.driver.find_element_by_id("com.coomix.app.car:id/item_title").click()  # 点击进入用户信息界面
        self.driver.find_element_by_id("com.coomix.app.car:id/btn_switch_account").click()  # 点击注销登录
        self.driver.find_element_by_id("com.coomix.app.car:id/btn_login").click()  # 点击登录按钮

    def test_send_note(self):
        # 登录功能
        self.driver.implicitly_wait(10)  # 全局等待10s
        # self.driver.find_element_by_id("com.coomix.app.car:id/tab_mine").click()  # 点击进入“我的”界面
        # self.driver.find_element_by_id("com.coomix.app.car:id/item_title").click()  # 点击进入用户信息界面
        # self.driver.find_element_by_id("com.coomix.app.car:id/btn_switch_account").click()  # 点击注销登录
        # self.driver.find_element_by_id("com.coomix.app.car:id/btn_login").click()  # 点击登录按钮
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_community").click()# 进入社区
        self.driver.find_element_by_id("com.coomix.app.car:id/actionbar_right").click()#点击右上角按钮，选择发帖或红包贴
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发个帖子']").click()#选择发普通贴
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='分享新鲜事...']").send_keys('sddasdas')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发送']").click()


    def test_send_redpack(self):
        self.driver.implicitly_wait(10)  # 全局等待10s
        # self.driver.find_element_by_id("com.coomix.app.car:id/tab_mine").click()  # 点击进入“我的”界面
        # self.driver.find_element_by_id("com.coomix.app.car:id/item_title").click()  # 点击进入用户信息界面
        # self.driver.find_element_by_id("com.coomix.app.car:id/btn_switch_account").click()  # 点击注销登录
        # self.driver.find_element_by_id("com.coomix.app.car:id/btn_login").click()  # 点击登录按钮
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_community").click()# 进入社区
        self.driver.find_element_by_id("com.coomix.app.car:id/actionbar_right").click()#点击右上角按钮，选择发帖或红包贴
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发红包帖']").click()#选择发红包贴
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='要发个红包，想说些什么？']").send_keys('asiuhajs')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='平台问题反馈']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='下一步']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='0.00']").send_keys('0.01')
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='填写个数']").send_keys('1')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='不限']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='500米']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='零钱(余额:0.04元)']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发出红包帖']").click()




    def tearDown(self):
        print u'测试完成'

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    #testsuite.addTest(Test('test_send_note'))
    testsuite.addTest(Test('test_send_redpack'))
    runner = unittest.TextTestRunner()
    runner.run(testsuite)

