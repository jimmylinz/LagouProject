#成员编辑页面
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.test_appium_work2.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    _edit_username_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    _edit_gender_element = (MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']")
    _edit_gender_element_female = (MobileBy.XPATH, "//*[@text='女']")
    _edit_gender_element_male = (MobileBy.XPATH, "//*[@text='男']")
    _edit_phonenum_element = (MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']")
    _click_save_element = (MobileBy.XPATH, "//*[@text='保存']")

    #编辑用户名
    def edit_username(self,username):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(username)
        # self.find(self._edit_username_element).send_keys(username)
        self.find_and_send(self._edit_username_element, username)
        return self

    #编辑性别
    def edit_gender(self,gender):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        # self.find(self._edit_gender_element).click()
        self.find_and_click(self._edit_gender_element)
        if gender == '女':
            # self.driver.find_element_by_xpath("//*[@text='女']").click()
            # self.find(self._edit_gender_element_male).click()
            self.find_and_click(self._edit_gender_element_female)
        else:
            # self.driver.find_element_by_xpath("//*[@text='男']").click()
            # self.find(self._edit_gender_element_female).click()
            self.find_and_click(self._edit_gender_element_male)
        return self

    #编辑电话号码
    def edit_phonenum(self,phonenum):
        self.find_and_send(self._edit_phonenum_element,phonenum)
        # self.find(self._edit_phonenum_element).send_keys(phonenum)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(phonenum)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.find_and_click(self._click_save_element)
        # self.find(self._click_save_element).click()
        from app.test_appium_work2.page.memberInvitepage import MemberInvitePage
        sleep(2)
        return MemberInvitePage(self.driver)