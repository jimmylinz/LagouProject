import json


import pytest
from filelock import FileLock

from test_work_request2.test_api.baseapi import BaseApi




class Wework(BaseApi):

    def token(self):
        data = {
            "method": "get",
            "url": "https://qytag.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwf82395f00fb65ebe",
                "corpsecret": "U97_3uPYGBl6mDeiGenHX9Ub0rB8oV4d5fDi59_qDWk"
            }
        }
        token = BaseApi.send_api(**data)
        try:
            return token['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    @pytest.fixture(scope='session')
    def get_token(self,tmp_path_factory,worker_id):
        if not worker_id:
            # not executing in with multiple workers, just produce the data and let
            # pytest's fixture caching do its job
            return self.token()

        # get the temp directory shared by all workers
        root_tmp_dir = tmp_path_factory.getbasetemp().parent

        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                data = json.loads(fn.read_text())
            else:
                data = self.token()
                fn.write_text(json.dumps(data))
        return data
