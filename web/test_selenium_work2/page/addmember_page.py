from selenium.webdriver.common.by import By

from web.test_selenium_work2.page.base_page import BasePage
from web.test_selenium_work2.page.contact_page import Contact

'''
def getdata():
    with open("data/member.yml") as f:
        datas_yml = yaml.safe_load(f)
    return datas_yml

@pytest.mark.parametrize(("usr","act","phone"),getdata())
'''

class AddMember(BasePage):

    _username = "username"#用户名输入框
    _acctid = "memberAdd_acctid"#账号输入框
    _phone = "memberAdd_phone"#手机号输入框
    _save = ".js_btn_save"#提交按钮
    _cancel = ".js_btn_cancel"#取消按钮

    def add_member(self):
        self.find(By.ID, self._username).send_keys("绝对5")
        self.find(By.ID, self._acctid).send_keys("0000013")
        self.find(By.ID, self._phone).send_keys("13520000004")
        self.find(By.CSS_SELECTOR, self._save).click()
        return Contact(self.driver)

    def add_member_fail(self):
        self.find(By.ID, self._username).send_keys("绝对2")
        self.find(By.ID, self._acctid).send_keys("000003")
        self.find(By.ID, self._phone).send_keys("13500000001")
        self.find(By.CSS_SELECTOR, self._save).click()
        self.find(By.CSS_SELECTOR, self._cancel).click()
        return Contact(self.driver)

