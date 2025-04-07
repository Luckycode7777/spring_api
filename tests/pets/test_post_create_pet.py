import allure

from config.base_test import BaseTest
from allure_commons.types import Severity
import requests
import json


@allure.epic('Pets')
class TestPositive(BaseTest):  # наследуем тестовый класс от BaseTest

    @allure.tag('api')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Maxy')
    @allure.feature('Задачи в репозитории')
    @allure.story("Создание нового юзера")
    @allure.title('Greate new user')
    def test_create_pet(self):
        # allure.dynamic.tag('API')
        # allure.dynamic.severity(Severity.CRITICAL)
        # allure.dynamic.label('owner', 'Maxi')
        # allure.dynamic.feature('Задачи в репозитории')
        # allure.dynamic.story('Создание нового юзера')
        # allure.dynamic.title('Greate new user')
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
