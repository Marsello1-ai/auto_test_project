from endpoint.get_authorize_token import MethodGetAuthorize
from endpoint.post_authorize import MethodPostAuthorize

"""
Единый класс для получения токенов
Главная функция: возвращает валидный токен
"""


class TokenManager:
    token = None
    post_authorize = MethodPostAuthorize()
    get_auth = MethodGetAuthorize()
    name = "Mars"

    def get_new_token(self):
        token_id = self.post_authorize.post_authorize(self.name)
        self.token = token_id
        return token_id

    def is_token_valid(self, token):
        status_code = self.get_auth.get_authorize(token)
        return status_code == 200

    def get_valid_token(self):
        # 1. Если токена нет, то получаем новый
        if not self.token:
            return self.get_new_token()

        # 2. Проверяем валидность живого токена
        if self.is_token_valid(self.token):
            return self.token
        else:
            return self.get_new_token()
