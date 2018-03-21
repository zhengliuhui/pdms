#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from dic import *


class AllPage(Dic):
    #alllist = (By.LINK_TEXT,u'所有包裹')
    searchbtn=(By.ID,'but_list_search')
    shippingno=(By.ID,'inp_shipping_no')
    queryconditions=(By.ID,'wordLikeType')
    bustype=(By.ID,'busType')
    packagestaus=(By.ID,'slt_package_staus')
    datatable=(By.ID,'dataTables-example')
    abnormalflag=(By.ID,'slt_package_abnormalFlag')
    checkbox=(By.XPATH,'//input[@name="shippingNos"]')
    pkgabnormal=(By.ID,'pkg_abnormal')
    pkgissuestaus=(By.XPATH,'//td[@abnormalflag="abnormalFlag"]')
#    pkgissuestaus=(By.CSS_SELECTOR,'.odd.gradeX>td')
    issuetype=(By.ID,'slt_parent_issue_type')
    issuereason=(By.ID,'slt_issue_desc')
    issuesubmit=(By.LINK_TEXT,u'保存')
    currentshippingno=(By.CSS_SELECTOR,'.odd.gradeX>td>a')
    pkgsignbtn=(By.ID,'pkg_sign_for')
    addressAttribute=(By.XPATH,"(//input[@name='addressAttribute'])[3]")
    fee=(By.XPATH,"(//input[@name='fee'])[2]")
    signsubmitbtn=(By.LINK_TEXT,u'确认')
    currentpkgstaus=(By.CSS_SELECTOR,'.layui-layer-content.layui-layer-padding')
    importbtn=(By.ID,'pkg_excel_top')
    exportbtn=(By.ID,'pkg_export')
    remarkCustomer=(By.NAME,'remarkCustomer')

    '''
    def click_all_list(self):
        #global dic
        #dic=Dic(self.driver)
        alllistbtn=self.find(AllPage.alllist)
        #alllistbtn=self.driver.find_element(*AllPage.alllist)
        alllistbtn.click()
    '''
    def click_search_btn(self):
        search_btn=self.find(AllPage.searchbtn)
        search_btn.click()

    def set_shipping_no(self,shippingno):
        shipping_no=self.driver.find_element(*AllPage.shippingno)
        shipping_no.send_keys(shippingno)

    def select_queryconditions_phone(self):
        query_conditions=self.driver.find_element(*AllPage.queryconditions)
        Select(query_conditions).select_by_value('BY_CONSIGNEE_PHONE')

    def set_bustype(self):
        setbustype=self.driver.find_element(*AllPage.bustype)
        Select(setbustype).select_by_value('TMALL-4PL')

    def set_package_staus(self):
        package_staus=self.driver.find_element(*AllPage.packagestaus)
        Select(package_staus).select_by_value('WAIT_IN_STORAGE')

    def data_table(self):
        data_table=self.driver.find_element(*AllPage.datatable)
        return data_table

    def set_slt_package_abnormalFlag(self):
        abnormal_flag=self.driver.find_element(*AllPage.abnormalflag)
        Select(abnormal_flag).select_by_value('F')

    def click_checkbox(self):
        check_box=self.driver.find_element(*AllPage.checkbox)
        check_box.click()

    def get_currentshippingno(self):
        current_shippingno=self.driver.find_element(*AllPage.currentshippingno)
        return current_shippingno.text

    def click_currentshippingno(self):
        current_shippingno_link=self.find(AllPage.currentshippingno)
        current_shippingno_link.click()

    def click_pkg_abnormal(self):
        pkg_abnormal=self.driver.find_element(*AllPage.pkgabnormal)
        pkg_abnormal.click()

    def get_pkgissuestaus(self):
        pkg_issuestaus=self.driver.find_element(*AllPage.pkgissuestaus)
        print u'异常状态：'+pkg_issuestaus.text
        return pkg_issuestaus.text

    def select_issuetype(self):
        issue_type=self.driver.find_element(*AllPage.issuetype)
        Select(issue_type).select_by_value('CUSTOMER_SIGNED_ABERRANT')

    def select_issuereason(self):
        issue_reason=self.driver.find_element(*AllPage.issuereason)
        Select(issue_reason).select_by_value('CANNOT_CONTACT')

    def click_issuesubmit(self):
        issue_submit=self.driver.find_element(*AllPage.issuesubmit)
        issue_submit.click()

    def click_pkgsign_btn(self):
        pkgsign_btn=self.driver.find_element(*AllPage.pkgsignbtn)
        pkgsign_btn.click()

    def click_addressAttribute(self):
        address_Attribute=self.driver.find_element(*AllPage.addressAttribute)
        address_Attribute.click()

    def click_fee(self):
        paied_additional_fee=self.driver.find_element(*AllPage.fee)
        paied_additional_fee.click()

    def click_signsubmitbtn(self):
        signsubmit_btn=self.driver.find_element(*AllPage.signsubmitbtn)
        signsubmit_btn.click()

    def assert_sign(self):
        assert_sign=self.driver.find_element(*AllPage.currentpkgstaus)
        return assert_sign.text

    def click_import(self):
        import_btn=self.find(AllPage.importbtn)
        import_btn.click()

    def click_export(self):
        export_btn=self.find(AllPage.exportbtn)
        export_btn.click()

    def set_remarkCustomer(self,remark):
        remark_Customer=self.find(AllPage.remarkCustomer)
        remark_Customer.clear()
        remark_Customer.send_keys(remark)

    packagebutedit=(By.ID,'package_but_edit')
    def click_package_but_edit(self):
        package_but_edit=self.find(AllPage.packagebutedit)
        package_but_edit.click()

    #operationrecordremark=(By.XPATH,'html/body/div[1]/div[1]/div/section[2]/div/div/div/div[2]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[6]')
    operationrecordremark=(By.XPATH,'//div[2]/div/div[2]/table/tbody/tr[1]/td[6]')
    def get_operationrecord_remark(self):
        operationrecord_remark=self.find(AllPage.operationrecordremark)
        return operationrecord_remark.text

    deliveryType=(By.ID,'slt_deliveryType_bar')
    def select_slt_deliveryType_bar(self):
        slt_deliveryType_bar=self.find(AllPage.deliveryType)
        Select(slt_deliveryType_bar).select_by_value('0')

'''

        driver.find_element_by_class_name("select2-selection__arrow").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/span/span/span[2]/ul/li[9]").click()
        driver.find_element_by_xpath("html/body/div[1]/div[1]/div/section[2]/div/div/form/div[1]/div[8]/div/span/span[1]/span/span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/span/span/span[2]/ul/li[13]").click()
        driver.find_element_by_id("but_list_search").click()
        time.sleep(2)
        driver.find_element_by_name("shippingNos").click()
        driver.find_element_by_id("pkg_sign_for").click()
        driver.find_element_by_name("addressAttribute").click()
        driver.find_element_by_link_text(u"确认").click()
        time.sleep(2)
        Select(driver.find_element_by_id("slt_package_abnormalFlag")).select_by_value("T")
        time.sleep(2)
        driver.find_element_by_id("but_list_search").click()
        time.sleep(8)

       #driver.find_element_by_id("pkg_export").click()

'''