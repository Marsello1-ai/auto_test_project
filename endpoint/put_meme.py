import requests
from faker import Faker
from endpoint.main_endpoint import MainEndpoint


class MethodPutMeme(MainEndpoint):

    def build_random_payload(self, meme_id):
        """Генерируем payload"""
        return {
            "id": meme_id,
            "text": Faker().sentence(nb_words=5),
            "url": Faker().image_url(),
            "tags": [Faker().word(), Faker().word()],
            "info": {
                "color": Faker().color_name(),
                "age": Faker().random_int(min=1, max=100),
            },
        }

    def put_meme(self, meme_id, token_id, payload: dict | None = None):
        """Главный метод, если payload не передается
        генерируем валидный build_random_payload"""
        if payload is None:
            payload = self.build_random_payload(meme_id)

        headers = {
            "Content-Type": "application/json",
            "Authorization": token_id,
        }
        self.response = requests.put(
            f"{self.url}meme/{meme_id}",
            json=payload,
            headers=headers,
        )
        return self.response

    def put_meme_negative(self, meme_id, token_id, payload: dict):
        headers = {
            "Content-Type": "application/json",
            "Authorization": token_id,
        }
        self.response = requests.put(
            f"{self.url}meme/{meme_id}",
            json=payload,
            headers=headers,
        )
        return self.response
