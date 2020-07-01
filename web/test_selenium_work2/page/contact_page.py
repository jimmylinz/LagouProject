import time

from selenium.webdriver.common.by import By

from web.test_selenium_work2.page.base_page import BasePage


class Contact(BasePage):
    _memberTable_td = ".member_colRight_memberTable_td"#通讯录用户信息行
    _number = '//*[@id="js_contacts263"]/div/div[2]/div/div[2]/div[1]/div[2]/span/span/span[2]'#人数
    _tb_member = ".member_colRight_memberTable_td_Checkbox"#定位到列表行
    _checkbox = ".ww_checkbox"#选择用户按钮
    _delete = ".js_delete"#删除按钮
    _submit = ".qui_btn ww_btn ww_btn_Blue"#确定按钮
    _cancel = "确认"#弹窗点击按钮元素

    def get_addmember(self):
        elements = self.finds(By.CSS_SELECTOR,self._memberTable_td)
        name_list =[element.get_attribute("title") for element in elements]
        return name_list

    def get_number(self):
        number = self.find(By.XPATH,self._number).text
        return number

    def delete_member(self):
        #定位到checkbox元素位置
        self.finds(By.CSS_SELECTOR,self._tb_member)
        time.sleep(3)
        #定位到checkbox元素选项并点击
        self.find(By.CSS_SELECTOR,self._checkbox).click()
        time.sleep(3)
        #点击删除按钮
        self.find(By.CSS_SELECTOR,self._delete).click()
        #点击弹窗确认删除
        self.find(By.LINK_TEXT,self._cancel).click()
        time.sleep(3)
        #重新查表用于断言校验
        elements = self.finds(By.CSS_SELECTOR, self._memberTable_td)
        name_list = [element.get_attribute("title") for element in elements]
        return name_list