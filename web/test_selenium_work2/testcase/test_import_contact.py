import xlrd as xlrd

from web.test_selenium_work2.page.main_page import MainPage


class TestImportcontact():
    def setup(self):
        self.main = MainPage()

    #校验上传文件是否正确
    def test_import(self):
        assert "import_member.xlsx" == self.main.goto_import_contact().import_contact_data()
        print("上传文件名展示正常")

    #校验通讯录是否上传成功
    def test_import_contact(self):
        # 打开excel文件，创建一个workbook对象,book对象也就是fruits.xlsx文件,表含有sheet名
        data = xlrd.open_workbook('E:\python_project\web/test_selenium_work2\data\member.yml')
        # 读取第一个表
        sheet = data.sheets()[0]
        # 读取第一列
        clou = sheet.col_values(0)
        # 除去标题，将姓名读取至data_clou
        data_clou = []
        for i in range(9,len(clou)):
            data_clou.append(clou[i])
            i = i+1
        assert print(set(data_clou)-set(self.main.goto_import_contact().import_contact().get_addmember()))==None
        print("导入成功")

    #校验通讯录上传失败的情况
    def test_import_contact_fail(self):
        mumber_after = self.main.goto_import_contact().import_contact_fail().get_addmember()
        assert self.main.goto_contact().get_addmember() == mumber_after
        print("导入失败")

    #校验上传的通讯录内容有相同信息的情况（用户名不同手机号相同）
    def test_import_contact_fail_exists(self):
        n_after = self.main.goto_import_contact().get_exists()
        assert print(set(n_after)-set(self.main.goto_contact().get_addmember()))==None
        print("导入内容有手机号重复")

    def teardown(self):
        self.main.quit()