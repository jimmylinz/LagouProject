import time

from selenium.webdriver.common.by import By

from web.selenium_frame_window.base import Base


class TestForm(Base):
    def test_windows(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])

        self.driver.find_element(By.ID,"TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("13000000000")
        time.sleep(3)

        self.driver.switch_to_window(window[0])
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__footerULoginBtn").click()
        time.sleep(3)

        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("13543303810")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("928sr410")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
        time.sleep(3)
