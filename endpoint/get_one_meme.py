import requests
from endpoint.main_endpoint import MainEndpoint


class MethodGetOneMeme(MainEndpoint):

    def get_one_meme(self, meme_id, token_id):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.response = requests.get(f'{self.url}meme/{meme_id}', headers=headers)

        return self.response

    def get_one_meme_negative_meme_id(self, token_id):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.response = requests.get(f'{self.url}meme/', headers=headers)

        return self.response

    def get_one_meme_negative_authorize(self, meme_id):
        headers = {'Content-Type': 'application/json', 'Authorization': None}
        self.response = requests.get(f'{self.url}meme/{meme_id}', headers=headers)

        return self.response
