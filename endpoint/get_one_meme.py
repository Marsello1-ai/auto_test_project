import requests
from endpoint.main_endpoint import MainEndpoint


class MethodGetOneMeme(MainEndpoint):

    def get_one_meme(self, meme_id, token_id):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.response = requests.get(f'{self.url}meme/{meme_id}', headers=headers)

        return self.response
