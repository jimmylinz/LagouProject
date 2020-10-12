from unittest import TestCase

from api.test_apirequest import test_request
from api.test_env_request import env_demo


class TestApi(TestCase):
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/demo.text",
        "heards": None
    }

    def test_send(self):
        api = env_demo.Api()
        print(api.send(self.data).text)