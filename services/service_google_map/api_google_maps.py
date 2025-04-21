from pprint import pprint

import requests

from config.http_methods import HttpMethods
from services.service_google_map.endpoints import Endpoints
from services.service_google_map.payloads import Payloads

"""Методы для тестирования Google maps api"""


class GoogleMapsAPI:
    def __init__(self):   # инициализировали все нужные объекты
        # self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    """Метода для создания новой локации"""
    @staticmethod
    def create_new_place():
        base_url = Endpoints.base_url  # базовый урл
        json_for_create_new_place = Payloads.json_create_new_place()  # тело запроса
        endpoint_post = Endpoints.resource_post  # ресурс метода post
        key = Endpoints.key  # квери параметры

        post_urt = f'{base_url}{endpoint_post}{key}'
        print(post_urt)

        result_post = HttpMethods.post(post_urt, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_place(place_id):
        base_url = Endpoints.base_url  # базовый урл
        endpoint_get = Endpoints.resource_get  # ресурс метода get
        key = Endpoints.key

        get_url = f'{base_url}{endpoint_get}{key}&place_id={place_id}'
        print(get_url)
        result_get = HttpMethods.get(get_url)
        pprint(result_get.text)
        return result_get

    """Метод для удаления локации"""
    @staticmethod
    def delete_new_place(place_id):
        base_url = Endpoints.base_url
        endpoint_delete = Endpoints.resource_delete
        key = Endpoints.key

        delete_url = f'{base_url}{endpoint_delete}{key}'
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, Payloads.json_delete_place(place_id))
        print(result_delete)
        return result_delete


