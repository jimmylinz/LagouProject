from selenium import webdriver
from selenium.webdriver.common.by import By

from web.test_selenium2.page.base_page1 import BasePage
from web.test_selenium2.page.contact_page1 import Contact
from selenium.webdriver.chrome.options import Options

class AddMember(BasePage):

    _username = "username"

    def add_member(self):
        self.find(By.ID,self._username).send_keys("东巴1")
        self.find(By.ID,"memberAdd_acctid").send_keys("000002")
        self.find(By.ID,"memberAdd_phone").send_keys("13543333332")
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return Contact(self.driver)

    def add_member_fail(self):
        self.find(By.ID,self._username).send_keys("东巴2")
        self.find(By.ID,"memberAdd_acctid").send_keys("000002")
        self.find(By.ID,"memberAdd_phone").send_keys("13543333332")
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return Contact(self.driver)



