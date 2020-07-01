import time

from selenium.webdriver.common.by import By

from web.test_selenium_work2.page.base_page import BasePage
from web.test_selenium_work2.page.contact_page import Contact


class ImportContactPage(BasePage):
    _input = '//*[@id="js_upload_file_input"]'#上传按钮
    _filename = "upload_file_name"#上传的文件名
    _submit = "submit_csv"#导入按钮
    _reupload = "reUpload"#重新上传按钮
    _import_black = "import_back_no_loading"#上传页面返回按钮
    _input_complete = "reloadContact"#完成按钮
    _black = "js_goBack"#失败返回按钮
    _data_url = "E:\python_project\web/test_selenium_work2\data\member.yml"  #通讯录导入路径
    _fail_data_url = "E:\python_project\web/test_selenium_work2\data/fail_contact.xlsx" #错误格式的通讯录路径
    _exists_fata_url = "E:\python_project\web/test_selenium_work2\data\exists_contact.xlsx" #内容已存在的通讯录路径
    _mumber_exists = ".import_table_td:nth-child(1)"#上传失败的用户名
    _import_table = ".import_table"#获取表格表头
    _error_list = "js_error_list"#获取表格所有数据

    def import_contact_data(self):
        self.find(By.XPATH,self._input).send_keys(self._data_url)
        fname = self.find(By.ID,self._filename).text
        return fname

    def import_contact(self):
        self.find(By.XPATH,self._input).send_keys(self._data_url)
        self.find(By.ID,self._submit).click()
        self.find(By.ID,self._input_complete).click()
        return Contact(self.driver)

    def import_contact_fail(self):
        self.find(By.XPATH,self._input).send_keys(self._fail_data_url)
        self.find(By.ID,self._submit).click()
        self.find(By.ID,self._reupload).click()
        self.find(By.ID, self._import_black).click()
        return Contact(self.driver)

    def import_contact_fail_exists(self):
        self.find(By.XPATH, self._input).send_keys(self._exists_fata_url)
        self.find(By.ID, self._submit).click()
        time.sleep(3)
        self.find(By.ID, self._black).click()
        return Contact(self.driver)

    #获取导入失败内容
    def get_exists(self):
        self.find(By.XPATH, self._input).send_keys(self._exists_fata_url)
        self.find(By.ID, self._submit).click()
        time.sleep(3)
        self.find(By.CSS_SELECTOR,self._import_table)
        #导入失败的内容赋给error_data
        error_data = self.find(By.ID,self._error_list).text
        #使用空格分隔数据并传入error_list
        error_list = error_data.split(" ")
        return error_list
