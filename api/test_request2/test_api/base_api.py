import requests


class BaseApi:
    def send_api(self,req:dict):
        return requests.request(**req).json()