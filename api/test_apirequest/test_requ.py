import json

import requests
import base64

def test_encode():
    url = "http://127.0.0.1:9999/demo.txt"
    r = requests.get(url=url)
    res = json.loads(base64.b64decode(r.content))
    print(res)