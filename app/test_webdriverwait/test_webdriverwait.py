import time


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestDW:
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'android'
        desire_caps['platformVersion'] = '6.0'
        desire_caps['deviceName'] = '127.0.0.1:7555'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desire_caps['noReset'] = 'true'
        desire_caps['dontStopAppOnReset'] = 'true'
        desire_caps['skipDeviceInitialization'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@text = '阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()

        locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        ele = WebDriverWait(self.driver, 10).until( lambda x: x.find_element(*locator))
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # ele = self.driver.find_element(*locator)
        print(ele.text)
        current_price = float(ele.text)
        expect_price = 170
        # assert current_price > expect_price
        assert_that(current_price,close_to(expect_price,expect_price*0.1))