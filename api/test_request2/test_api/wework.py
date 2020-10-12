import requests

from api.test_request2.test_api.base_api import BaseApi


class WeWork(BaseApi):
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