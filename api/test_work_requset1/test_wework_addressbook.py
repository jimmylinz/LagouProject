import requests



class TestWework:

    session = requests.Session()

    def test_setup(self):
        param = {
            'corpid' : "wwf82395f00fb65ebe",
            'corpsecret' : "U97_3uPYGBl6mDeiGenHX9Ub0rB8oV4d5fDi59_qDWk"
        }
        r = self.session.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params = param)
        self.session.params.update({"access_token":r.json()['access_token']})
        print(r.json())

    def test_add(self):
        date = {
            "userid": "zhangsan23312",
            "name": "张三213",
            "mobile": "13800002333",
            "department": [1]
        }
        r = self.session.post('https://qyapi.weixin.qq.com/cgi-bin/user/create',json = date)
        print(r.json())
        assert r.json()['name'] == "张三213"

    def test_get(self):
        params = {
            "userid": "1231321"
        }
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_update(self):
        date = {
            "userid": "1231321",
            "name":"三十三"
        }
        r = self.session.post("https://qyapi.weixin.qq.com/cgi-bin/user/update", json=date)
        print(r.json())
        assert r.json()['name'] == "三十三"

    def test_delete(self):
        params = {
            "userid": "1231321",
        }
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        print(r.json())
        assert r.json()['errcode'] == 0