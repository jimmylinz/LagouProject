from selenium.webdriver.common.by import By

from web.test_pageobject.page.base_page import BasePage


class Regiester(BasePage):
    def regiester(self):
        self.find(By.ID,"corp_name").send_keys("hello")
        self.find(By.ID,"manager_name").send_keys("hello2")
        return True