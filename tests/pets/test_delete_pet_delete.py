import requests
import json
import pytest


# @pytest.mark.skip
def test_delete_pet_delete():
    url = "https://petstore.swagger.io/v2/pet/7717"

    payload = {}
    headers = {
      'api_key': 'abc123'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)
