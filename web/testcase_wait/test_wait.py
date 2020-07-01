from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Testwait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element_by_id("ember41").click()
        # self.driver.find_element_by_link_text("linkText=所有分类").click()
        def wait(x):
            return len(self.driver.find_element_by_id("ember230")) >= 1
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element_by_id("ember150").click()

