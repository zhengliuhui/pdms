#coding=utf-8
from test.base import Login

__author__ = 'liuhui'

import unittest
import time
import sys

from test.base import Login
from test.page.DashBoard import DashBoard
from test.page.AllPage import AllPage
from test.base.Logger import log

reload(sys)
sys.setdefaultencoding("utf-8")


class Test_All(unittest.TestCase):

    login= Login.Login()
    dr = login.test_Login()

    def setUp(self,driver=dr):
        self.driver=driver
        #login= Login.Login()
        #self.driver = login.test_Login()
        dashboard=DashBoard(self.driver)
        dashboard.click_delivery_list()
        time.sleep(2)
        if dashboard.isElementExist(u'所有包裹'):
            dashboard.click_all_list()
        else:
            dashboard.click_delivery_list()
            time.sleep(2)
            dashboard.click_all_list()
        time.sleep(2)
        global allpage
        #allpage=AllPage(self.driver)
        allpage=AllPage(self.driver)
        #allpage.click_all_list()
        time.sleep(2)

    #查询包裹
    def test_Search(self):
        allpage.set_bustype()
        allpage.set_package_staus()
        time.sleep(2)
        allpage.click_search_btn()
        log.info(u"查询成功")


    #标记异常
    def test_Abnormalflag(self):
        allpage.select_queryconditions_phone()
        allpage.set_shipping_no('15622108520')
        allpage.set_slt_package_abnormalFlag()
        allpage.click_search_btn()
        time.sleep(2)
        allpage.click_checkbox()
        shippingno=allpage.get_currentshippingno()
        print u'标记异常单号：'+shippingno
        allpage.click_pkg_abnormal()
        time.sleep(2)
        allpage.select_issuetype()
        time.sleep(2)
        allpage.select_issuereason()
        allpage.click_issuesubmit()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        allpage.set_shipping_no(shippingno)
        allpage.click_search_btn()
        time.sleep(3)
        pkgissuestaus=allpage.get_pkgissuestaus()
        print pkgissuestaus
        if pkgissuestaus==u'是':
            #self.assertEqual(pkgissuestaus,u'是')
            log.info(u"标记异常成功")
        else:
            log.info(u'标记异常失败')

    #批量签收
    def test_Pkgsign(self):
        allpage.select_queryconditions_phone()
        allpage.set_shipping_no('15622108520')
        allpage.set_package_staus()
        allpage.click_search_btn()
        time.sleep(2)
        allpage.click_checkbox()
        shippingno=allpage.get_currentshippingno()
        print u'包裹签收单号：'+shippingno
        allpage.click_pkgsign_btn()
        time.sleep(2)
        allpage.click_addressAttribute()
        time.sleep(2)
        allpage.click_fee()
        allpage.click_signsubmitbtn()
        time.sleep(1)
        assertpkgstaus=allpage.assert_sign()
        self.assertEqual(assertpkgstaus,u'包裹签收成功')
        log.info(u"包裹签收成功")

    #包裹详情
    def test_pkgdetail(self):
        #获得当前窗口
        nowhandle=self.driver.current_window_handle
        #allpage.select_slt_deliveryType_bar()
        allpage.click_search_btn()
        time.sleep(1)
        currentshippingno=allpage.get_currentshippingno()
        allpage.click_currentshippingno()
        #获得所有窗口
        allhandles=self.driver.window_handles
        #循环判断窗口是否为当前窗口
        for handle in allhandles:
            if handle !=nowhandle:
                self.driver.switch_to_window(handle)
                time.sleep(2)
                pkgdetailno=self.driver.find_element_by_id("shippingNo").text
                print u'点击单号'+currentshippingno,u'包裹详情单号'+pkgdetailno
                self.assertEqual(currentshippingno,pkgdetailno)
                time.sleep(2)
                log.info(u'打开包裹详情页')

                #测试包裹备注
                allpage.click_package_but_edit()
                time.sleep(1)
                allpage.set_remarkCustomer(u'测试包裹备注')
                allpage.click_package_but_edit()
                time.sleep(5)
                operationrecord_remark=allpage.get_operationrecord_remark()
                print operationrecord_remark
                self.assertEqual(operationrecord_remark,u'测试包裹备注')
                log.info(u'包裹备注成功')

                #测试短信重发
                try:
                    self.driver.find_element_by_id('but_note_resend').click()
                    time.sleep(5)
                    operationrecord_remark=allpage.get_operationrecord_remark()

                    if u'重发成功' in operationrecord_remark:
                        print u'短信重发成功'
                        log.info(u'短信重发成功')
                    else:
                        print u'短信重发失败'
                        log.info(u'短信重发失败')
                except:
                    print u'没有短信重发按钮'
                    log.info(u'没有短信重发按钮')

                self.driver.close()
                log.info(u'关闭包裹详情页')
        #回到原先的窗口
        self.driver.switch_to_window(nowhandle)
        time.sleep(3)

    def test_zzz_quit(self):
        self.driver.quit()
        #self.driver.close()

    def tearDown(self):
        try:
            self.driver.refresh()#将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
        except:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
