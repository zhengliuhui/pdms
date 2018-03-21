#coding=utf-8
from test.base import Login

__author__ = 'liuhui'

import unittest

from test.base import Login
from test.page.DashBoard import DashBoard
from test.base.Logger import log


class Test_DashBoard(unittest.TestCase):

    login= Login.Login()
    dr = login.test_Login()

    def setUp(self,driver=dr):
        self.driver=driver
        #login= Login.Login()
        #self.driver = login.test_Login()

    #左侧列表
    def test_dashboard(self):
        dashboard=DashBoard(self.driver)
        dashboard.click_delivery_list()
        log.info(u"展开派件业务")
        #time.sleep(1)
        dashboard.click_all_list()
        log.info(u"所有包裹")
        #time.sleep(1)
        dashboard.click_issue_list()
        log.info(u"异常件处理")
        #time.sleep(1)
        dashboard.click_customer_list()
        log.info(u"展开客服管理")
        #time.sleep(1)
        dashboard.click_customer_search_list()
        log.info(u"客服查件")
        #time.sleep(1)
        dashboard.click_customer_processing_issue_list()
        log.info(u"异常件待处理")
        #time.sleep(1)
        dashboard.click_customer_processed_issue_list()
        log.info(u"异常件已处理")
        #time.sleep(1)

    def test_zzz_quit(self):
        self.driver.quit()
        #self.driver.close()

    def tearDown(self):
        try:
            self.driver.refresh()#将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
        except:
            self.driver.quit()

#    def tearDown(self):
#        self.driver.close()