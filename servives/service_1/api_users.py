import allure
import requests

from config.headers import Headers
from servives.service_1.payloads import Payloads
from servives.service_1.endpoints import Endpoints

from utils.helper import Helper


class UsersAPI(Helper):
    def __init__(self):  # инициализировали все нужные объекты
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Create a new user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.get_users,
            headers=self.headers.basic_headers,
            json=self.payloads.create_user()
        )
        assert response.status_code == 200, f'Невалидный статус код - {response.status_code} \n {response.json()}'

        log = f""" 
        REQUEST:
            URL: {response.request.url}
            METHOD: {response.request.method}
            JSON: {response.request.body}

        RESPONSE:
            STATUS_CODE: {response.status_code}
            CONTENT: {response.content}
        """
        print('\n********************')
        print(f'ЛОГИРОВАНИЕ: {log}')
        assert response.status_code == 200
        self.attach_response(response.json())
        # assert response.json()['id'] == 7717
        # assert response.json()['name'] == "Mars"



