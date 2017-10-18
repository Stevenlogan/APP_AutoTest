#coding:utf-8
import os
from OpenApp import *
import sys
reload(sys)
sys.setdefaultencoding('gbk')
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


open_app = OpenApp('CJL5T15C11015231')
driver = open_app.open_app()

driver.implicitly_wait(10)#全局等待10s

#登录功能
driver.find_element_by_id("com.coomix.app.car:id/tab_mine").click()#点击进入“我的”界面
driver.find_element_by_id("com.coomix.app.car:id/item_title").click()#点击进入用户信息界面
driver.find_element_by_id("com.coomix.app.car:id/btn_switch_account").click()#点击注销登录
# driver.find_element_by_id("com.coomix.app.car:id/et_account").clear()#清空账户输入框
# driver.find_element_by_id("com.coomix.app.car:id/et_pass").clear()#清空密码输入框
# driver.find_element_by_id("com.coomix.app.car:id/et_account").send_keys("ywyyb")#输入账户
# driver.find_element_by_id("com.coomix.app.car:id/et_pass").send_keys("ywyyb")#输入密码
driver.find_element_by_id("com.coomix.app.car:id/btn_login").click()#点击登录按钮

#进入app操作
driver.find_element_by_id("com.coomix.app.car:id/tab_community").click()#点击社区，登录社区账号，否则无法接受消息
driver.find_element_by_id("com.coomix.app.car:id/tab_info").click()#切换至消息界面
driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='1']").click()#点击进入聊天群

#具体操作
i = 0
f = open('C:\Users\pc1412002\Desktop/1.txt','r')
l = f.readlines()
f.close()

# with open('C:\Users\pc1412002\Desktop/1.txt','r') as f:
#     l = f.readlines()
    #f.close()
while i <= 10000000:
    for m in l:
        driver.find_element_by_id("com.coomix.app.car:id/edittext_layout").send_keys(m.decode('utf8'))
        driver.find_element_by_id("com.coomix.app.car:id/btn_send").click()
        # driver.find_element_by_id("com.coomix.app.car:id/iv_face_normal").click()#点击打开表情界面
        # driver.find_element_by_id("com.coomix.app.car:id/iv_expression").click()#选择表情
        # driver.find_element_by_id("com.coomix.app.car:id/btn_send").click()#发送
    print i
    i += 1
