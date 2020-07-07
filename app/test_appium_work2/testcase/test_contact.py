import pytest
import yaml

from app.test_appium_work2.page.app import App

#用户数据驱动
with open ("../data/contacts.yml",encoding="UTF-8") as f:
    datas_yml = yaml.safe_load(f)
    print(datas_yml)
    addlist = datas_yml['add']
    dellist = datas_yml['delete']

class TestWeWork:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()


    # @pytest.mark.parametrize('username,gender,phonenum',addlist)
    def test_addcontact(self):
        username = "qwe"
        gender = '男'
        phonenum = '13532211100'
        #添加联系人的业务逻辑
        toast = self.main.goto_addresslist().click_addmember().addmember_menual()\
            .edit_username(username).edit_gender(gender).edit_phonenum(phonenum).click_save().get_result()

        assert "添加成功" == toast
        self.main.back()

    @pytest.mark.parametrize('user',dellist)
    def test_delcontact(self,user):
        list = self.main.goto_addresslist().click_delmember().delmember_menual(user).delete_mumber().get_list(user)
        assert user not in list
        self.main.back()

    def testdown_class(self):
        self.app.close()

