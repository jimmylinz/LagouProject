
#添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from app.test_appium_work2.page.basepage import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    _addmember_menual_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _get_result_element = (MobileBy.XPATH, "//*[@class = 'android.widget.Toast']")

    #选择手动添加
    def addmember_menual(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # self.find(self._addmember_menual_element).click()
        self.find_and_click(self._addmember_menual_element)
        from app.test_appium_work2.page.contactaddpage import ContactAddPage
        return ContactAddPage(self.driver)

    #获取toast
    def get_result(self):
        # tosttext = self.driver.find_element(MobileBy.XPATH, "//*[@class = 'android.widget.Toast']").text
        # tosttext = self.find(self._get_result_element).text
        tosttext = self.get_toast()
        return tosttext