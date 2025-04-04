import allure

from config.base_test import BaseTest
import requests
import json


@allure.epic('Framework N-2')
class TestPositive(BaseTest):  # наследуем тестовый класс от BaseTest

    @allure.title('Greate new user')
    def test_create_pet(self):
        self.api_users.create_user()
        print('\n TEST END GOOD ************')

        # log = f"""
        # REQUEST:
        #     URL: {response.request.url}
        #     METHOD: {response.request.method}
        #     JSON: {response.request.body}
        #
        # RESPONSE:
        #     STATUS_CODE: {response.status_code}
        #     CONTENT: {response.content}
        # """
        #
        # print(f'\n ЛОГИРОВАНИЕ:\n{log}')
        # assert response.status_code == 200
        # assert response.json()['id'] == 7717
        # assert response.json()['name'] == "Mars"
