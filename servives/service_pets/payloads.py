import random

from faker import Faker

faker = Faker()  # создали объект класса Faker


class Payloads:

    @staticmethod
    def json_create_user():
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


