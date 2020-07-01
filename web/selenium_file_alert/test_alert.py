import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element(By.ID,"draggable")
        drop = self.driver.find_element(By.ID,"droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        time.sleep(3)
        print("获取alert")
        self.driver.switch_to_alert().accept()
        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.ID,"submitBTN").click()
        time.sleep(3)