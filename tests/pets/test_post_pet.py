import allure
import time

from allure_commons.types import Severity
from utils.cheking import Checking
from services.service_pets.api_users import UsersAPI
from services.service_pets.payloads import Payloads


@allure.epic('Pets')
class TestPositive:

    @allure.tag('api')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Maxy')
    @allure.feature('Задачи в репозитории')
    @allure.story("Создание, получение, удаление нового юзера")
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
        user_id = check_post.get('id', 'Такого ключа нет')
        print(f'USER ID **>> {user_id}')
        Checking.checking_status_code(result_post, 200)
        Checking.check_json_values(result_post, Checking.get_keys(result_post))
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
        result_get = UsersAPI.get_user_id(user_id)
        Checking.checking_status_code(result_get, 200)
        Checking.check_json_values(result_get, Checking.get_keys(result_get))

        print('\n метод DELETE')
        result_delete = UsersAPI.delete_nem_user(user_id)
        Checking.checking_status_code(result_delete, 200)
        Checking.check_json_values(result_delete, Checking.get_keys(result_delete))

        print('\n метод GET DELETE')
        result_get = UsersAPI.get_user_id(user_id)
        Checking.checking_status_code(result_get, 404)
        Checking.check_json_values(result_get, Checking.get_keys(result_get))

    def test_delete_user_id(self):
        user_id = Payloads.create_user_id()
        time.sleep(3)
        """просто DELETE"""
        print('\n просто DELETE')

        result_delete = UsersAPI.delete_nem_user(user_id)
        time.sleep(3)
        Checking.checking_status_code(result_delete, 200)
        Checking.check_json_values(result_delete, Checking.get_keys(result_delete))

