import time

from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get("http://image.baidu.com/")
        self.driver.find_element(By.XPATH,'//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID,"uploadImg").send_keys("E:\python_project\img/1593441873.jpg")
        time.sleep(3)