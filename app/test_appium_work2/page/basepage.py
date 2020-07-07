from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    #fend_element封装
    def find(self,locator):
        return self.driver.find_element(*locator)

    #fends_element封装
    def finds(self,locator):
        return self.driver.find_elements(*locator)

    #uiselector封装
    def find_by_scroll(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                                                                            .scrollIntoView(new UiSelector()\
                                                                            .text("{text}").instance(0));')
    #click封装
    def find_and_click(self,locator):
        self.find(locator).click()

    #sendkeys封装
    def find_and_send(self,locator,text):
        self.find(locator).send_keys(text)

    #获取toast封装
    def get_toast(self):
        return self.driver.find_element(MobileBy.XPATH, "//*[@class = 'android.widget.Toast']").text

    #显示等待封装
    def waitdriverwait_nountil(self,text,timeout):
        return WebDriverWait(self.driver,15).until_not(lambda x: x.find_element_by_xpath(f"//*[@text='{text}']"))
        # return WebDriverWait(self.driver,15).until_not(expected_conditions.visibility_of_element_located(id))

    #返回封装
    def back(self,num=1):
        for i in range(num):
            self.driver.back()
