import requests
import json
import pytest


# @pytest.mark.skip
def test_rename_pet_put():
    url = "https://petstore.swagger.io/v2/pet"

    payload = json.dumps({
      "id": 7717,
      "category": {
        "id": 17,
        "name": "planet"
      },
      "name": "Marsy",
      "photoUrls": [
        "https://goo.su/qTF5qa0"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
