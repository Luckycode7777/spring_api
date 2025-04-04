import requests
import json
import pytest


@pytest.mark.skip
def test_get_pet_get():
    url = "https://petstore.swagger.io/v2/pet/7717"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)