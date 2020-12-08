import random

import requests


class BaseApi:

    def send_tag(self,req:dict):
        return requests.request(**req).json()

    def create_date(self):
        data = [str(random.randint(0,999999999)),"user1"]
        return data

    def create_muti_data(self):
        data = [("1001" + str(x),"wu" + str(x))for x in range(20)]
        return data
