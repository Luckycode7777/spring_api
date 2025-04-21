import requests


class Checking:
    """Метод для проверки статус кода"""
    @staticmethod
    def checking_status_code(result, status_code):
        assert status_code == result.status_code, f'Неверный статус код - {status_code}'
        print(f"Успешно! Статус код = {result.status_code}")
