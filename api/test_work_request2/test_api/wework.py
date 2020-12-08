from api.test_work_request2.test_api.baseapi import BaseApi


class Wework(BaseApi):

    def get_token(self):
        date = {
            "method":"get",
            "url":"https://qytag.weixin.qq.com/cgi-bin/gettoken",
            "params" : {
                "corpid": "wwf82395f00fb65ebe",
                "corpsecret": "U97_3uPYGBl6mDeiGenHX9Ub0rB8oV4d5fDi59_qDWk"
            }
        }
        token = self.send_tag(date)
        try:
            return token['access_token']
        except Exception as e:
            raise ValueError("requests token error")