import time

import allure

from utils.http_methods import HttpMethods
from services.service_pets.endpoints import Endpoints
from services.service_pets.payloads import Payloads
from utils.headers import Headers


class UsersAPI:
    def __init__(self):  # инициализировали все нужные объекты
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    """Создание нового пользователя"""
    @staticmethod
    @allure.step("Create a new user")
    def create_user():
        base_url = Endpoints.base_url
        json_for_create_new_id = Payloads.json_create_user()  # тело запроса

        response_post = HttpMethods.post(base_url, json_for_create_new_id)
        print(f'++++++++++++ RSP POST ***>>> {response_post}')
        assert response_post.status_code == 200, f'Невалидный статус код - {response_post.status_code} \n {response_post.json()}'
        print(response_post.text)
        time.sleep(3)
        # log = f"""
        # REQUEST:
        #     URL: {response_post.request.url}
        #     METHOD: {response_post.request.method}
        #     JSON: {response_post.request.body}
        #
        # RESPONSE:
        #     STATUS_CODE: {response_post.status_code}
        #     CONTENT: {response_post.content}
        # """
        # print('\n********************')
        # print(f'ЛОГИРОВАНИЕ: {log}')
        return response_post

    """Получение ID нового пользователя"""
    @staticmethod
    def get_user_id(user_id):
        base_url = Endpoints.base_url

        get_url = f'{base_url}{user_id}'
        time.sleep(1)
        result_get = HttpMethods.get(get_url)
        if result_get.status_code == 404:
            result_get = HttpMethods.get(get_url)
            if result_get.status_code == 404:
                result_get = HttpMethods.get(get_url)
        print(result_get.url)
        # print(result_get.status_code)
        # print(result_get.text)
        return result_get

    """Удаление нового пользователя"""
    @staticmethod
    def delete_nem_user(user_id):
        base_url = Endpoints.base_url

        delete_url = f'{base_url}{user_id}'
        result_delete = HttpMethods.delete(delete_url, body=None)
        print(delete_url)
        print(result_delete.status_code)
        print(result_delete.text)
        # print(result_delete.json())
        return result_delete


