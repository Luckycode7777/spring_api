import requests
from utils.headers import Headers
from utils.cookies import Cookie


class HttpMethods:
    def __init__(self):
        self.headers = Headers
        self.cookie = Cookie

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Headers.basic_headers, cookies=Cookie.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Headers.basic_headers, cookies=Cookie.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Headers.basic_headers, cookies=Cookie.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Headers.basic_headers, cookies=Cookie.cookie)
        return result
