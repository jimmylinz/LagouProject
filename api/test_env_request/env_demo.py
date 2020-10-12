import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yml"))
    def send(self,data:dict):
        #替换
        data["url"] = str(data["url"]).replace("testing-studio",self.env["testing-studio"][self.env["default"]])

        r = requests.request(method=data["method"],url=data["url"],headers=data["headers"])
        return r