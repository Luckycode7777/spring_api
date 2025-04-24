import random
import json

from services.service_pets.endpoints import Endpoints
from utils.http_methods import HttpMethods

from faker import Faker

faker = Faker()  # создали объект класса Faker


class Payloads:
    @staticmethod
    def json_create_user():  # Создание json юзера
        ids = random.randint(100, 10000)
        json_user = {
            "id": ids,
            "category": {
                "id": 17,
                "name": f"planet_{faker.name()}"
            },
            "name": f"{faker.user_name()}_{ids}",
            "photoUrls": [
                "https://goo.su/qTF5qa0"
            ]
        }
        return json_user

    """Создание нового user_id"""
    @staticmethod
    def create_user_id():
        base_url = Endpoints.base_url
        ids = random.randint(100, 10000)
        json_user = {
            "id": ids,
            "category": {
                "id": 17,
                "name": f"planet_{faker.name()}"
            },
            "name": f"{faker.user_name()}_{ids}",
            "photoUrls": [
                "https://goo.su/qTF5qa0"
            ]
        }
        response = HttpMethods.post(base_url, json_user)
        # user_id = json_user.get("id", 'Такого ключа нет')
        print(f"##### response.json()[id] ####>>>> {response.json()['id']}")
        return response.json()['id']


