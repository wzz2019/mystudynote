import requests

from requests.auth import HTTPBasicAuth

class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.org/get')
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code==200

    def test_query(self):
        payload={
            "level":1,
            "name":"aaa"
        }
        r = requests.get('http://httpbin.org/get',params=payload)
        print(r.text)
        assert r.status_code==200

    def test_post(self):
        payload={
            "level":1,
            "name":"aaa"
        }
        r = requests.post('http://httpbin.org/post',data=payload)
        print(r.text)
        assert r.status_code==200

    def test_headers(self):
        payload = {
            "name": "aaa"
        }
        r = requests.get('http://httpbin.org/get', headers=payload)
        print(r.text)
        # print(r.json()["headers"])
        assert r.status_code == 200
        assert r.json()["headers"]["Name"]=="aaa"

    def test_json(self):
        payload={
            "level":1,
            "name":"aaa"
        }
        r = requests.post('http://httpbin.org/post',json=payload)
        print(r.text)
        assert r.status_code==200

    def test_cookies1(self):
        url='http://httpbin.org/cookies'
        header={"Cookies":"name=aaa;school=bbb"}
        r=requests.get(url=url,headers=header)
        print(r.request.headers)

    def test_cookies2(self):
        url='http://httpbin.org/cookies'
        cookie_data={"name":"aaa","school":"bbb"}
        r=requests.get(url=url,cookies=cookie_data)
        print(r.request.headers)

    def test_auth(self):
        url="http://httpbin.org/basic-auth/user001/passwd001"
        r=requests.get(url=url,
                       auth=HTTPBasicAuth("user001","passwd001"))
        assert r.status_code==200
        r=requests.get(url=url,
                       auth=HTTPBasicAuth("user002","passwd002"))
        assert r.status_code==200