from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAcion:
    class TestDW:
        def setup(self):
            desire_caps = {}
            desire_caps['platformName'] = 'android'
            desire_caps['platformVersion'] = '6.0'
            desire_caps['deviceName'] = '127.0.0.1:7555'
            desire_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
            desire_caps['appActivity'] = 'com.samsung.ui.MainActivity'
            desire_caps['noReset'] = 'true'
            desire_caps['dontStopAppOnReset'] = 'true'
            desire_caps['skipDeviceInitialization'] = 'true'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self.driver.implicitly_wait(20)


        def teardown(self):
            # self.driver.back()
            # self.driver.back()
            self.driver.quit()

        def test_touch_unlck(self):
            action = TouchAction(self.driver)
            action.press(x=133,y=193).wait(200).move_to(x=406,y=193).wait(200).move_to(x=687,y=193).wait(200).move_to(x=687,y=474).wait(200).move_to(x=687,y=733).release().perform()
