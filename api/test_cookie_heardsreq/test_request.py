import requests


def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        'User-Agent':'hogwarts'
              }
    cookies_data = {
        "hogwarts":"school",
        "teacher":"ming"
    }
    r = requests.get(url=url,headers = header,cookies = cookies_data)
    print(r.request.headers)