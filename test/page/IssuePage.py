#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from test.page.BasePage import BasePage


class IssuePage(BasePage):
    issuelist = (By.LINK_TEXT,u'异常件处理')
    searchbtn=(By.ID,'but_list_search')
    shippingno=(By.ID,'inp_shipping_no')
    queryconditions=(By.ID,'wordLikeType')
    datatable=(By.ID,'dataTables-example')
    abnormalflag=(By.ID,'slt_issue_abnormal')
    checkbox=(By.XPATH,'//input[@name="shippingNos"]')

    def click_issue_list(self):
        issuelistbtn=self.driver.find_element(*IssuePage.issuelist)
        issuelistbtn.click()

    def click_search_btn(self):
        search_btn=self.driver.find_element(*IssuePage.searchbtn)
        search_btn.click()

    def set_shipping_no(self,shippingno):
        shipping_no=self.driver.find_element(*IssuePage.shippingno)
        shipping_no.send_keys(shippingno)

    def select_queryconditions_phone(self):
        query_conditions=self.driver.find_element(*IssuePage.queryconditions)
        Select(query_conditions).select_by_value('BY_CONSIGNEE_PHONE')

    def data_table(self):
        data_table=self.driver.find_element(*IssuePage.datatable)
        return data_table

    def set_slt_issue_abnormal(self):
        abnormal_flag=self.driver.find_element(*IssuePage.abnormalflag)
        Select(abnormal_flag).select_by_value('T')

    def click_checkbox(self):
        check_box=self.driver.find_element(*IssuePage.checkbox)
        check_box.click()



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