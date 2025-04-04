from servives.service_1.api_users import UsersAPI


class BaseTest():
    """Инициализация всех объектов папки serviсes"""
    def setup_method(self):
        self.api_users = UsersAPI()


