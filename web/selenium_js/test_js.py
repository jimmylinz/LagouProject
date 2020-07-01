import time

import pytest
from selenium.webdriver.common.by import By

from web.selenium_js.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,"kw").send_keys("test")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop = 10000")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="page"]/div/a[10]').click()
        time.sleep(3)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        # print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))