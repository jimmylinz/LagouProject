from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def finds(self,locator):
        return self.driver.find_elements(*locator)

    def find_by_scroll(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                                                                            .scrollIntoView(new UiSelector()\
                                                                            .text("{text}").instance(0));')

    def find_and_click(self,locator):
        self.find(locator).click()

    def find_and_send(self,locator,text):
        self.find(locator).send_keys(text)

    def get_toast(self):
        return self.driver.find_element(MobileBy.XPATH, "//*[@class = 'android.widget.Toast']").text

    def waitdriverwait_nountil(self,text,timeout):
        return WebDriverWait(self.driver,15).until_not(lambda x: x.find_element_by_xpath(f"//*[@text='{text}']"))
        # return WebDriverWait(self.driver,15).until_not(expected_conditions.visibility_of_element_located(id))

    def back(self,num=1):
        for i in range(num):
            self.driver.back()
