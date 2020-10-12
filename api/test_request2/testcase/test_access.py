import random
import re

import pytest
import requests

from api.test_request2.test_api.access import Access
from api.test_request2.test_api.wework import WeWork


class TestAccess:
    @pytest.fixture(scope="session")
    def token(self):
        yield WeWork().test_get_token()

    def setup(self):
        self.access = Access()

    def creat_muit_data(self):
        data = [("aaaa" + str(x),"zhangsan1","138%08d" % x)for x in range(20)]
        return data

    @pytest.mark.parametrize("userid,name,mobile",creat_muit_data("xx"))
    def test_all(self,userid,name,mobile,token):
        try:
            #创建一个成员，对结果断言
            assert "created" == self.access.test_add(userid,name,mobile,token)['errmsg']
        except AssertionError as e:
            if "userid existed" in e.__str__():
                self.access.test_delete(userid,token)
            if "mobile existed" in e.__str__():
                delete_userid = re.findall(":(.*)'$",e.__str__())
                self.access.test_delete(delete_userid,token)
            assert "created" == self.access.test_add(userid,name,mobile,token)['errmsg']
        #查询成员信息，对结果断言
        assert name == self.access.test_get(userid,token)['name']
        #更新一个成员
        assert "updataed" == self.access.test_updata(userid,"wangwu",token)['errmsg']
        assert "wangwu" == self.access.test_get(userid,token)['name']
        #删除
        assert "delete" == self.access.test_delete(userid,token)['errmsg']
        assert 60111 == self.access.test_get(userid,token)['errcode']

    def test_session(self,token):
        s = requests.Session()
        s.params = {"access_token":token}
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "userid": "zhangsan"
            }

        }
        s.request(**data).json()