import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

def getdata():
    with open ("member.yml",encoding="UTF-8") as f:
        datas_yml = yaml.safe_load(f)
    return datas_yml

class TestTouchAcion:
    class TestDW:
        def setup(self):
            desire_caps = {}
            desire_caps['platformName'] = 'android'
            desire_caps['platformVersion'] = '6.0'
            desire_caps['deviceName'] = '127.0.0.1:7555'
            desire_caps['appPackage'] = 'com.tencent.wework'
            desire_caps['appActivity'] = '.launch.WwMainActivity'
            desire_caps['noReset'] = True
            desire_caps['skipDeviceInitialization'] = True
            desire_caps['resetKeyboard'] = 'true'
            desire_caps['unicodeKeyboard'] = 'true'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()

        def teardown(self):
            self.driver.quit()

        @pytest.mark.parametrize("username,sex,phonenum",getdata().get("add"))
        def test_addcontact(self,username,sex,phonenum):
            gender = sex
            self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                                                            .scrollIntoView(new UiSelector()\
                                                            .text("添加成员").instance(0));').click()
            self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
            self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(username)
            self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/..//*[@text='男']").click()
            if gender == '女':
                self.driver.find_element_by_xpath("//*[@text='女']").click()
            else:
                self.driver.find_element_by_xpath("//*[@text='男']").click()
            self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(phonenum)
            self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
            # print(self.driver.page_source)
            tosttext = self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']").text
            assert tosttext == '添加成功'
            print("添加成功")


        @pytest.mark.parametrize("user",getdata().get("delete"))
        def test_delcontact(self,user):
            self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/h9u").click()
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                                                            .scrollIntoView(new UiSelector()\
                                                            .text("{user}").instance(0));').click()
            self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
            eles = self.driver.find_elements(MobileBy.XPATH,
                                             "//*[@resource-id='com.tencent.wework:id/hfg']/..//*[@class='android.widget.TextView']")
            del_list = [ele.get_attribute("text") for ele in eles]
            assert user not in del_list
            print("删除成功")

if __name__ == "__main__":
    pytest.main()