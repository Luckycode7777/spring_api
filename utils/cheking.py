import json

import requests


class Checking:

    """Метод для проверки статус кода"""
    @staticmethod
    def checking_status_code(result, status_code):
        assert status_code == result.status_code, f'Неверный статус код - {status_code}'
        print(f"Успешно! Статус код = {result.status_code}")

    """Метод для проверки наличия обязательных полей(keys) в ответе запроса"""
    @staticmethod
    def check_json_keys(result, expected_result):
        fields = json.loads(result.text)  # result.json()
        assert list(fields) == expected_result, 'ERROR, Список полей не совпадает'
        print(list(fields))
        print("Все поля присутствуют")

    """Метод для получения обязательных полей(keys) в ответе"""
    @staticmethod
    def get_keys(result):
        fields = json.loads(result.text)
        fields = [k for k, v in fields.items()]
        return fields

    """Метод для проверки значений(values) обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_values(result, fild_name, expected_value):
        check = result.json()  # хотим видеть ответ(результат) в виде json строки
        check_info = check.get(fild_name)   # возвращаем значение поля fild_name
        assert check_info == expected_value
        print(f'fild_name >> - {fild_name} - ВЕРЕН')

    """Метод для получения обязательных полей(keys) в ответе"""
    @staticmethod
    def get_value(result):
        fields = json.loads(result.text)
        fields = [v for k, v in fields.items()]
        return fields

