from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from app.test_appium_work2.page.basepage import BasePage
from app.test_appium_work2.page.main import MainPage


class App(BasePage):
    driver:WebDriver
    def start(self):
        _package = 'com.tencent.wework'
        _activity = '.launch.WwMainActivity'

        if self.driver == None:
            desire_caps = {}
            desire_caps['platformName'] = 'android'
            desire_caps['deviceName'] = '127.0.0.1:7555'
            desire_caps['appPackage'] = _package
            desire_caps['appActivity'] = _activity
            desire_caps['noReset'] = 'True'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub",desire_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    #关闭测试
    def close(self):
        self.driver.quit()

    #进入主页
    def main(self):
        return MainPage(self.driver)