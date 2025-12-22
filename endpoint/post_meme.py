import requests
from endpoint.main_endpoint import MainEndpoint


class MethodPostMeme(MainEndpoint):
    meme_id = None
    payload = None

    def post_meme_for_fixture(self, token_id):
        payload = {
            "text": "fsdfsdf",
            "url": "https://upload.wikimedia.org/wikipedia/ru/a/a3/%D0%A3%D0%BF%D0%BE%D1%80%D0%BE%D1%82%D1%8B%D0%B9_%D0%BB%D0%B8%D1%81.jpeg",
            "tags": ["eqwewq", "adasdad"],
            "info": {"color": "white", "age": 25}
        }
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.response = requests.post(f'{self.url}meme', json=payload, headers=headers)
        self.meme_id = self.response.json()['id']

        return self.meme_id

    def post_meme(self, token_id, payload):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.payload = payload
        self.response = requests.post(f'{self.url}meme', json=payload, headers=headers)

        return self.response

    def check_payload_post_meme(self):
        body = self.response.json()
        assert body["text"] == self.payload["text"]
        assert body["url"] == self.payload["url"]
        assert body["tags"] == self.payload["tags"]
        assert body["info"] == self.payload["info"]
