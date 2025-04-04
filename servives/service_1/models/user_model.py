from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list


response = {
    "id": 0,
    "category": {
        "id": 17,
        "name": "string"
    },
    "name": "string",
    "photoUrls": [
        "string"
    ]
}

user = UserModel(**response)
