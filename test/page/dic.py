#coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from test.page.BasePage import BasePage
import time

class Dic(BasePage):

    def find(self,loc):
        element=self.driver.find_element(*loc)
        return element

    def isElementExist(self,element):
        flag=True
        try:
            self.driver.find_element_by_link_text(element)
            return flag

        except:
            flag=False
            return flag
"""
    def find_elements(self,loc):
        '''
        find elements.
        Usage:
        driver.find_elements((By.XPATH,"//a"))
        '''
        try:
            WebDriverWait(self.driver,self.timeout).until(lambda drive:drive.find_elements(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception,e:
            print u"%s 页面中超时%ds未能找到 %s 元素%s" %(self,self.timeout,loc,e)
 
    def click_keys(self,loc):
        '''
        click keys
        Usage:
        driver.click_keys((By.XPATH,"//a"))
        '''
        self.find(loc).click()
 
    def clear_keys(self,loc):
        '''
        clear keys
        Usage:
        driver.clear_keys((By.XPATH,"//a"))
        '''
        self.find(loc).clear()
 
    def send_keys(self,loc,value):
        '''
        send keys
        Usage:
        send_keys((By.XPATH,"//a"),'a')
        '''
        time.sleep(3)
        self.clear_keys(loc)
        self.find(loc).send_keys(value)
 
    def click_button(self,loc):
        '''
        click button
        Usage:
        click_button((By.XPATH,"//a"))
        '''
        time.sleep(3)
        self.find(loc).click()
 
    def script(self,src):
        '''
        execute_script
        Usage:
        script(src)
        '''
        return self.driver.execute_script(src)
 
    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.
        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)
 
    def set_window(self, wide, high):
        '''
        Set browser window wide and high.
        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)
 
    def right_click(self, loc):
        '''
        Right click element.
        Usage:
        driver.right_click((By.XPATH,"//a"))
        '''
        el = self.find(loc)
        ActionChains(self.driver).context_click(el).perform()
 
    def move_to_element(self, loc):
        '''
        Mouse over the element.
        Usage:
        driver.move_to_element((By.XPATH,"//a"))
        '''
        el = self.find(loc)
        ActionChains(self.driver).move_to_element(el).perform()
 
    def double_click(self, loc):
        '''
        Double click element.
        Usage:
        driver.double_click((By.XPATH,"//a"))
        '''
        el = self.find(loc)
        ActionChains(self.driver).double_click(el).perform()
 
    def drag_and_drop(self, loc1, loc2):
        '''
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop((By.XPATH,"//a"),(By.XPATH,"//b"))
        '''
        element  = self.find(loc1)
        target  = self.find(loc2)
        ActionChains(self.driver).drag_and_drop(element , target).perform()
 
    def get_display(self, loc):
        '''
        Gets the element to display,The return result is true or false.
        Usage:
        driver.get_display(By.XPATH,"//a")
        '''
        el = self.find(loc)
        return el.is_displayed()
 
    def isElement(self,identifyBy,c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        time.sleep(1)
        flag=None
        try:
            if identifyBy == "id":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException,e:
            flag = False
        finally:
            return flag
 
    def refresh(self):
        '''
        refresh  page
        Usage:
        driver.refresh
        '''
        self.driver.implicitly_wait(10)
        self.driver.refresh()
 
    def list_to_str(self,string):
        '''
        string to unicode
        Usage:
        list_to_str(str)
        '''
        str_symptom = str(string).replace('u\'','\'')
        return str_symptom.decode("unicode-escape")
 
    def get_text(self,loc):
        '''
        get text
        Usage:
        get_text(By.XPATH,"//a")
        '''
        time.sleep(3)
        return self.find(loc).text
 
    def get_url(self,url):
        '''
        get url
        Usage:
        get_url(url)
        '''
        time.sleep(3)
        return self.driver.get(url)
 
    def get_title(self,url):
        '''
        get title
        Usage:
        get_title(url):
        '''
        self.driver.get(url)
        return self.driver.title
"""

