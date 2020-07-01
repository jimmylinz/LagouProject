from selenium import webdriver
from selenium.webdriver.common.by import By

from web.test_selenium2.page.add_menber_page1 import AddMember
from web.test_selenium2.page.base_page1 import BasePage
from web.test_selenium2.page.contact_page1 import Contact


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_contact(self):
        return Contact(self.driver)