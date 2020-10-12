import requests
from requests.auth import HTTPBasicAuth

def test_auth():
    r = requests.get(url= "https://httpbin.testing-studio.com/basic-auth/aaa/123",
                     auth = HTTPBasicAuth("aaa","123"))
    print(r.text)