import requests
from endpoint.main_endpoint import MainEndpoint


class MethodPostAuthorize(MainEndpoint):
    token_id = None
    user_name = None

    def post_authorize(self, name):
        payload = {
            "name": name
        }

        self.response = requests.post(f'{self.url}authorize', json=payload, headers=self.headers)
        if self.response.status_code == 200:
            self.token_id = self.response.json()["token"]
            return self.token_id
            # Для 400 ничего не парсим, просто возвращаем None
        return None

    def check_user_name(self, name):
        assert self.response.json()['user'] == name
