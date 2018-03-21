#coding=utf-8
import time

from selenium import webdriver

from test.base.Logger import log



class Login():

    def test_Login(self):
        driver = webdriver.Chrome()
        #driver.maximize_window()
        self.base_url = "https://sso.test.i4px.com:8443/login?service=http://pds.test.i4px.com/pdms/login"
        driver.get(self.base_url)
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("s7001")
        driver.find_element_by_id("passwordOrg").clear()
        driver.find_element_by_id("passwordOrg").send_keys("123456pwd")
        driver.find_element_by_id("signbtn").click()

     #   log=Logger("test.log")
        time.sleep(2)

        now_url=driver.current_url
        dashboard_url="http://pds.test.i4px.com/pdms/dashboard"
       # return driver


        if now_url!=dashboard_url:
            log.info(u"系统登录成功")
            return driver

        else:
            log.error(u"系统登录失败")
            self.driver.quit()
