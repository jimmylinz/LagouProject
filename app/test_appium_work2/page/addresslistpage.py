from appium.webdriver.common.mobileby import MobileBy

from app.test_appium_work2.page.basepage import BasePage
from app.test_appium_work2.page.memberInvitepage import MemberInvitePage

#通讯录页面
from app.test_appium_work2.page.membermanagepage import MemberManagePage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    _addmember_text = "添加成员"
    _delmember_text = (MobileBy.ID,"com.tencent.wework:id/h9u")

    #点击添加成员
    def click_addmember(self):
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0))\
        #                                                             .scrollIntoView(new UiSelector()\
        #                                                             .text("添加成员").instance(0));').click()
        self.find_by_scroll(self._addmember_text).click()
        return MemberInvitePage(self.driver)

    #点击删除成员
    def click_delmember(self):
        self.find_and_click(self._delmember_text)
        return MemberManagePage(self.driver)