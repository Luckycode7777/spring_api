import requests
import json
import pytest

from services.service_pets.api_users import UsersAPI

# from servives.service_pets.api_users import

k = UsersAPI.create_user


# @pytest.mark.skip

def test_get_pet_get():
    url = f"https://petstore.swagger.io/v2/pet/{UsersAPI.create_user}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(f'**** >>>>> {response.text}')
    print(response.json())
