import time

from appium import webdriver


class TestTouchAcion:
    class TestDW:
        def setup(self):
            desire_caps = {}
            desire_caps['platformName'] = 'android'
            desire_caps['platformVersion'] = '6.0'
            desire_caps['deviceName'] = '127.0.0.1:7555'
            desire_caps['appPackage'] = 'com.tencent.wework'
            desire_caps['appActivity'] = '.launch.WwMainActivity'
            desire_caps['noReset'] = 'true'
            desire_caps['dontStopAppOnReset'] = 'true'
            desire_caps['skipDeviceInitialization'] = 'true'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self.driver.implicitly_wait(20)


        def teardown(self):
            # self.driver.back()
            # self.driver.back()
            self.driver.quit()

        def test_addcontact(self):
            # ele = self.driver.find_element_by_id("com.tencent.wework:id/dyx")
            # print(ele)
            # print(len(ele))
            # ele[2].click()
            # self.driver.find_element_by_name("通讯录")
            # time.sleep(3)
            username = "姓名2"
            gender = '男'
            phonenum = '13532321322'

            self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
            self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                                                            .scrollIntoView(new UiSelector()\
                                                            .text("添加成员").instance(0));').click()
            self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
            self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(username)
            self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()
            if gender == '女':
                self.driver.find_element_by_xpath("//*[@text='女']").click()
            else:
                self.driver.find_element_by_xpath("//*[@text='男']").click()
            self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(phonenum)
            self.driver.find_element_by_xpath("//*[@text='保存']").click()
            time.sleep(3)
            print(self.driver.page_source)
            tosttext = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
            assert tosttext == '添加成功'


