from time import sleep

from appium import webdriver


class Testattr:
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'android'
        desire_caps['platformVersion'] = '6.0'
        desire_caps['deviceName'] = '127.0.0.1:7555'
        desire_caps['noReset'] = True
        desire_caps['browserName'] = 'Browser'
        # desire_caps['chromedriverExecutable'] = 'C:\Users\林小鸟\Desktop'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
