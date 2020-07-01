import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_dbclick = self.driver.find_element(By.XPATH,'//*[@value="dbl click me"]')
        element_click = self.driver.find_element(By.XPATH,'//*[@value="click me"]')
        element_right_click = self.driver.find_element(By.XPATH, '//*[@value="right click me"]')
        action = ActionChains(self.driver)
        action.double_click(element_dbclick)
        action.click(element_click)
        action.context_click(element_right_click)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element(By.ID,"s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(5)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag = self.driver.find_element(By.ID,"dragger")
        drop1 = self.driver.find_element(By.XPATH,"html/body/div[2]")
        drop2 = self.driver.find_element(By.XPATH, "html/body/div[3]")
        drop3 = self.driver.find_element(By.XPATH, "html/body/div[4]")
        drop4 = self.driver.find_element(By.XPATH, "html/body/div[5]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop1).perform()
        action.drag_and_drop(drag,drop2).perform()
        action.drag_and_drop(drag,drop3).perform()
        # action.click_and_hold(drag).release(drop2).perform()
        action.drag_and_drop(drag, drop4).perform()
        # action.click_and_hold(drag).release(drop4).perform()

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH,'//*[@type="textbox"]')
        ele.click()
        action = ActionChains(self.driver).pause(1)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)
