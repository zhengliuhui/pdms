#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test.page.BasePage import BasePage


class LoginPage(BasePage):
    """description of class"""

    #page element identifier
    usename = (By.ID,'username')
    password = (By.ID, 'passwordOrg')
    dialogTitle = (By.CLASS_NAME,'nav-title')
    cancelButton = (By.ID,'li_fm_pkg')
    #dialogTitle = (By.XPATH,'//html/body/div[7]/div/div/div[1]/h3')
    #cancelButton = (By.XPATH,'//html/body/div[7]/div/div/div[3]/button[2]')

    #Get username textbox and input username
    def set_username(self,username):
        name = self.driver.find_element(*LoginPage.usename)
        name.send_keys(username)
   
    #Get password textbox and input password, then hit return
    def set_password(self, password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password + Keys.RETURN)

    #Get pop up dialog title
    def get_DiaglogTitle(self):
        digTitle = self.driver.find_element(*LoginPage.dialogTitle)
        return digTitle.text
    #Get pop up dialog title

    #Get "cancel" button and then click
    def click_cancel(self):
        cancelbtn = self.driver.find_element(*LoginPage.cancelButton)
        cancelbtn.click()
