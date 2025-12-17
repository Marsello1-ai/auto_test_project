import requests
from endpoint.main_endpoint import MainEndpoint


class MethodGetMeme(MainEndpoint):

    def get_meme(self, token_id):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.response = requests.get(f'{self.url}meme', headers=headers)

        return self.response
