import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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

    def test_dw(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text = '阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    def test_attr(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_element = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_element == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text = '阿里巴巴']")
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        time.sleep(10)
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height*4/5)
        y_end = int(height*1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text = '阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"股票价格为{current_price}")
        assert float(current_price)>200

    #uiselector定位
    def test_myinfo(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    #滚动定位
    def test_scroll_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true)'
                                                        '.instance(0)).scrollIntoView(new UiSelector()'
                                                        '.text("薇薇庄主").instance(0));').click()
        time.sleep(5)

if __name__ == '__main__':
    pytest.main()