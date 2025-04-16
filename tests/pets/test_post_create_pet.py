import allure
import time

from allure_commons.types import Severity
from servives.service_pets.api_users import UsersAPI


@allure.epic('Pets')
class TestPositive:  # наследуем тестовый класс от BaseTest

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
        print('\n метод POST')
        result_post = UsersAPI.create_user()
        check_post = result_post.json()
        print(f'CHECK POST **>> {check_post}')
        print('\n TEST END GOOD ************')
        user_id = check_post.get('id')
        print(f'USER ID **>> {user_id}')
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

        print('\n метод GET')
        UsersAPI.get_user_id(user_id)
        time.sleep(2)
        UsersAPI.get_user_id(user_id)

        # print(result_get1.status_code)
        # print(result_get1.text)


