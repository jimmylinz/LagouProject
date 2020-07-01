
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from web.test_selenium2.page.base_page1 import BasePage


class Contact(BasePage):

    def get_member(self):

        elements = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td")
        name_list =[element.get_attribute("title") for element in elements]
        return name_list
