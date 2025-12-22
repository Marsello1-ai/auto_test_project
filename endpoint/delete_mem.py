import requests
from endpoint.main_endpoint import MainEndpoint


class MethodDeleteMem(MainEndpoint):

    def delete_mem(self, meme_id, token_id):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}

        self.response = requests.delete(
            f'{self.url}meme/{meme_id}',
            headers=headers
        )

        return self.response.status_code

    def delete_mem_negative_meme_id(self, token_id):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}

        self.response = requests.delete(
            f'{self.url}meme/',
            headers=headers
        )

        return self.response.status_code
