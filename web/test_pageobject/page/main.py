
from selenium.webdriver.common.by import By

from web.test_pageobject.page.base_page import BasePage
from web.test_pageobject.page.login import Login
from web.test_pageobject.page.regiester import Regiester


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def goto_regiest(self):
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Regiester(self._driver)


    def goto_login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self._driver)