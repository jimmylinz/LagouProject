from selenium.webdriver.common.by import By

from web.test_pageobject.page.base_page import BasePage
from web.test_pageobject.page.regiester import Regiester


class Login(BasePage):
    def scan(self):
        pass

    def login_regiester(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Regiester(self._driver)