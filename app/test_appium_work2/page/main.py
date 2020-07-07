from appium.webdriver.common.mobileby import MobileBy

from app.test_appium_work2.page.addresslistpage import AddressListPage

#主页
from app.test_appium_work2.page.basepage import BasePage


class MainPage(BasePage):
    _addlist_element = (MobileBy.XPATH,"//android.widget.TextView[@text='通讯录']")
    # def __init__(self,driver):
    #     self.driver = driver

    #进入到通讯录
    def goto_addresslist(self):
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        self.find_and_click(self._addlist_element)
        return AddressListPage(self.driver)

    def goto_message(self):
        pass

    def goto_workbench(self):
        pass
