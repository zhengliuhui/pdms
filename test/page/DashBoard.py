#coding=utf-8
from selenium.webdriver.common.by import By

from test.page.dic import *

class DashBoard(Dic):

    #派件业务
    delivery = (By.LINK_TEXT,u'派件业务')
    def click_delivery_list(self):
        deliverybtn = self.driver.find_element(*DashBoard.delivery)
        deliverybtn.click()

    #所有包裹
    alllist = (By.LINK_TEXT,u'所有包裹')
    def click_all_list(self):
        alllistbtn=self.find(DashBoard.alllist)
        alllistbtn.click()

    #异常件处理
    issuelist = (By.LINK_TEXT,u'异常件处理')
    def click_issue_list(self):
        issuelist_btn=self.find(DashBoard.issuelist)
        issuelist_btn.click()

    #客服管理
    customer= (By.LINK_TEXT,u'客服管理')
    def click_customer_list(self):
        customer_btn = self.driver.find_element(*DashBoard.customer)
        customer_btn.click()

    #客服查件
    customersearchlist = (By.LINK_TEXT,u'客服查件')
    def click_customer_search_list(self):
        customer_search_list_btn=self.find(DashBoard.customersearchlist)
        customer_search_list_btn.click()

    #异常件待处理
    customer_processing_issue_list = (By.LINK_TEXT,u'异常件待处理')
    def click_customer_processing_issue_list(self):
        customer_processing_issue_list_btn=self.find(DashBoard.customer_processing_issue_list)
        customer_processing_issue_list_btn.click()

    #异常件已处理
    customer_processed_issue_list = (By.LINK_TEXT,u'异常件已处理')
    def click_customer_processed_issue_list(self):
        customer_processed_issue_list_btn=self.find(DashBoard.customer_processed_issue_list)
        customer_processed_issue_list_btn.click()

