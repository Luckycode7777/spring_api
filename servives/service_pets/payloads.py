import random

from faker import Faker
from random import randint

faker = Faker()  # создали объект класса Faker


class Payloads:

    def create_user(self):
        ids = random.randint(100, 10000)
        return {
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


print(Payloads().create_user())
