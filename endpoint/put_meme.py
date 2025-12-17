import requests
from endpoint.main_endpoint import MainEndpoint


class MethodPutMeme(MainEndpoint):

    def put_meme(self, meme_id, token_id):
        payload = {
            "id": meme_id,
            "text": "fsdfsdf",
            "url": "gfg",
            "tags": ["eqwewq", "adasdad"],
            "info": {"color": "white", "age": 25}
        }
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.response = requests.put(f'{self.url}meme/{meme_id}', json=payload, headers=headers)

        return self.token_id
