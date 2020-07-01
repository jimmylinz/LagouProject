from selenium.webdriver.common.by import By

from web.test_selenium_work2.page.addmember_page import AddMember
from web.test_selenium_work2.page.base_page import BasePage
from web.test_selenium_work2.page.contact_page import Contact
from web.test_selenium_work2.page.import_contact_page import ImportContactPage


class MainPage(BasePage):
    _add_mb = ".index_service_cnt_itemWrap:nth-child(1)"#添加成员按钮
    _import_ct = ".index_service_cnt_itemWrap:nth-child(2)"#导入通讯录按钮
    _ct = "menu_contacts"#跳转通讯录按钮

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR,self._add_mb).click()
        return AddMember(self.driver)

    def goto_contact(self):
        self.find(By.ID, self._ct).click()
        return Contact(self.driver)

    def goto_import_contact(self):
        self.find(By.CSS_SELECTOR,self._import_ct).click()
        return ImportContactPage(self.driver)



