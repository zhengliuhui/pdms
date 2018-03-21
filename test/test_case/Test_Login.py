#coding=utf-8
__author__ = 'liuhui'

import unittest
import time
from selenium import webdriver
from test.page.LoginPage import LoginPage
from test.base.Logger import log


class Test_Login(unittest.TestCase):

    dr = webdriver.Chrome()

    def setUp(self,driver=dr):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = "http://pds.test.i4px.com/pdms/dashboard"
  
    def test_Login(self):
        try:
            #Step1: open base site
            self.driver.get(self.base_url)
            #Step2: Open Login page
            login_page = LoginPage(self.driver)
            #Step3: Enter username
            login_page.set_username("s7001")
            #Step4: Enter password
            time.sleep(2)
            login_page.set_password("123456pwd")
            time.sleep(2)
            currenturl=self.driver.current_url
            print currenturl
            self.assertEqual(currenturl,"http://pds.test.i4px.com/pdms/dashboard","Equal")
            log.info("login")
        except:
            log.info("fail")

    def test_zzz_quit(self):
        self.driver.quit()
        #self.driver.close()

    def tearDown(self):
        try:
            self.driver.refresh()#将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
        except:
            self.driver.quit()

    #tearDown
#    def tearDown(self):
#        self.driver.close()

if __name__ == "__main__":
    unittest.main()
