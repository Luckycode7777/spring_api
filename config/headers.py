import os
from dotenv import load_dotenv

load_dotenv()


class Headers:

    basic_headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }

    """Для динамических хедеров"""
    def basic_dinamic_headers(self, value="token"):
        return {
            'accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {os.getenv('TOKEN')}",
            'X-Task-Id': {value}
        }
