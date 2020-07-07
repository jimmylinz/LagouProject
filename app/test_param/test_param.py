import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class Testparam:
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'android'
        desire_caps['platformVersion'] = '6.0'
        desire_caps['deviceName'] = '127.0.0.1:7555'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desire_caps['noReset'] = True
        desire_caps['skipDeviceInitialization'] = True
        desire_caps['resetKeyboard'] = 'true'
        desire_caps['unicodeKeyboard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        # self.driver.quit()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('searchkey,type,expect_price',[
        ('alibaba','BABA',220),
        ('小米','01810',14)
    ])
    def test_search(self,searchkey,type,expect_price):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        price_element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # expect_price = 220
        current_price = float(price_element.text)
        print(f"当前价格{current_price}")
        assert_that(current_price,close_to(expect_price,expect_price*0.1))