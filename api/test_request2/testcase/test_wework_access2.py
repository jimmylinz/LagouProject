import random
import re

import pytest
import requests


class TestWeworkAccess:

    @pytest.fixture(scope="session")
    def token(self):
        params = {
            "corpid" : "wwf82395f00fb65ebe",
            "corpsecret" : "U97_3uPYGBl6mDeiGenHXw8uRTfoDkEg2sxxL5XcXNs"
        }
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                           params=params)
        try:
            yield res.json()['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    def test_get_token(self):
        params = {
            "corpid": "wwf82395f00fb65ebe",
            "corpsecret": "U97_3uPYGBl6mDeiGenHXw8uRTfoDkEg2sxxL5XcXNs"
        }
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                           params=params)
        try:
            return res.json()['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    def test_add(self,userid,name,mobile,token,department=None):
        if department is None:
            department = [1]
        data = {
            "userid":userid,
            "name":name,
            "mobile":mobile,
            "department":department
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
                            ,json=data
                            )
        return res.json()

    def test_get(self,userid,token):
        params = {
            "access_token":token,
            "userid":userid
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        print(res.json())

    def test_updata(self,userid,name,token):
        data = {
            "userid":userid,
            "name":name
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                           json=data)
        return res.json()

    def test_delete(self,userid,token):
        params = {
            "access_token": token,
            "userid":userid
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        print(res.json())

    def create_data(self):
        data = [(str(random.randint(0,999999)),
                 "zhangsan1",
                 str(random.randint(13800000000,13899999999))
                 )for x in range(3)]
        return data

    def creat_muit_data(self):
        data = [("aaaa" + str(x),"zhangsan1","138%08d" % x)for x in range(20)]
        return data

    @pytest.mark.parametrize("userid,name,mobile",creat_muit_data("xx"))
    def test_all(self,userid,name,mobile,token):
        try:
            #创建一个成员，对结果断言
            assert "created" == self.test_add(userid,name,mobile,token)['errmsg']
        except AssertionError as e:
            if "userid existed" in e.__str__():
                self.test_delete(userid,token)
            if "mobile existed" in e.__str__():
                delete_userid = re.findall(":(.*)'$",e.__str__())
                self.test_delete(delete_userid,token)
            assert "created" == self.test_add(userid,name,mobile,token)['errmsg']
        #查询成员信息，对结果断言
        assert name == self.test_get(userid,token)['name']
        #更新一个成员
        assert "updataed" == self.test_updata(userid,"wangwu",token)['errmsg']
        assert "wangwu" == self.test_get(userid,token)['name']
        #删除
        assert "delete" == self.test_delete(userid,token)['errmsg']
        assert 60111 == self.test_get(userid,token)['errcode']
