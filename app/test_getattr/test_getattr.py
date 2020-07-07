from appium import webdriver
from hamcrest import *

class Testattr:
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

    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
        assert "search" in search_ele

    def test_assert(self):
        a = 10
        b = 20
        # assert a > b
        assert 'h' in 'this'

    def test_hamcrest(self):
        # assert_that( 10 , equal_to(9),'这是一个提示')
        # 10上下浮动2
        # assert_that( 13 , close_to( 10 , 2))
        #断言包含string
        assert_that("contaions some string", contains_string("string"))
