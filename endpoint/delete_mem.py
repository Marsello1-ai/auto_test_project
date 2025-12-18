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

    def delete_mem_negative_authorize(self, meme_id):
        headers = {'Content-Type': 'application/json', 'Authorization': None}

        self.response = requests.delete(
            f'{self.url}meme/{meme_id}',
            headers=headers
        )

        return self.response.status_code

    def check_negative_status_code_is_400(self):
        assert self.response.status_code == 404

    def check_negative_status_code_is_401(self):
        assert self.response.status_code == 401
