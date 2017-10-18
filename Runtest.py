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
        #启动App
        self.driver.implicitly_wait(10)  # 全局等待10s
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_mine").click()  # 点击进入“我的”界面
        self.driver.find_element_by_id("com.coomix.app.car:id/item_title").click()  # 点击进入用户信息界面
        self.driver.find_element_by_id("com.coomix.app.car:id/btn_switch_account").click()  # 点击注销登录
        self.driver.find_element_by_id("com.coomix.app.car:id/btn_login").click()  # 点击登录按钮


    #普通帖子发送功能
    def test_send_note(self):
        self.driver.implicitly_wait(10)  # 全局等待10s
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_community").click()# 进入社区
        self.driver.find_element_by_id("com.coomix.app.car:id/actionbar_right").click()#点击右上角按钮，选择发帖或红包贴
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发个帖子']").click()#选择发普通贴
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='分享新鲜事...']").send_keys('sddasdas')#输入帖子内容
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发送']").click()#点击发送按钮发送帖帖子



    def test_send_redpack(self):
        self.driver.implicitly_wait(10)  # 全局等待10s
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_community").click()# 进入社区
        self.driver.find_element_by_id("com.coomix.app.car:id/actionbar_right").click()#点击右上角按钮，选择发红包贴
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发红包帖']").click()#选择发红包贴
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='要发个红包，想说些什么？']").send_keys('asiuhajs')#填写帖子内容
        self.driver.find_element_by_xpath("//android.widget.Button[@text='平台问题反馈']").click()#选择帖子归属版块
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='下一步']").click()#完成帖子内容部分，进入红包信息界面
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='0.00']").send_keys('0.01')#填写红包金额
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='填写个数']").send_keys('1')#填写红包个数
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='不限']").click()#弹出红包范围选择界面
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='500米']").click()#选择红包范围
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='零钱(余额:0.04元)']").click()#选择支付方式
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='发出红包帖']").click()#点击发送

    #聊天群发送消息功能
    def test_send_IMMessage(self):
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_community").click()  # 点击社区，登录社区账号，否则无法接受消息
        self.driver.find_element_by_id("com.coomix.app.car:id/tab_info").click()  # 切换至消息界面
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='1']").click()  # 点击进入聊天群

        # 具体操作
        i = 0
        f = open('./TestData.txt', 'r')
        l = f.readlines()
        f.close()

        while i <= 10000000:
            for m in l:
                self.driver.find_element_by_id("com.coomix.app.car:id/edittext_layout").send_keys(m.decode('utf8'))
                self.driver.find_element_by_id("com.coomix.app.car:id/btn_send").click()
                # driver.find_element_by_id("com.coomix.app.car:id/iv_face_normal").click()#点击打开表情界面
                # driver.find_element_by_id("com.coomix.app.car:id/iv_expression").click()#选择表情
                # driver.find_element_by_id("com.coomix.app.car:id/btn_send").click()#发送
            print i
            i += 1



    def tearDown(self):
        print u'测试完成'

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    #testsuite.addTest(Test('test_send_note'))
    testsuite.addTest(Test('test_send_IMMessage'))
    runner = unittest.TextTestRunner()
    runner.run(testsuite)

