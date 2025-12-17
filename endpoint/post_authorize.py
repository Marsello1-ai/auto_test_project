import requests
from endpoint.main_endpoint import MainEndpoint


class MethodPostAuthorize(MainEndpoint):
    token_id = None

    def post_authorize(self):
        payload = {
            "name": "Mars"
        }
        self.response = requests.post(f'{self.url}authorize', json=payload, headers=self.headers)
        self.token_id = self.response.json()["token"]

        return self.token_id



