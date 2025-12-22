import requests
from faker import Faker
from endpoint.main_endpoint import MainEndpoint


class MethodPutMeme(MainEndpoint):
    payload = None
    meme_id = None

    @staticmethod
    def build_random_payload(meme_id):
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
            self.payload = payload
            self.meme_id = meme_id

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

    def check_payload_put_meme(self):
        body = self.response.json()
        print(f'{body["id"]}')
        print(f'{self.meme_id}')
        assert body["id"] == self.payload["id"]
        assert body["text"] == self.payload["text"]
        assert body["url"] == self.payload["url"]
        assert body["tags"] == self.payload["tags"]
        assert body["info"] == self.payload["info"]
