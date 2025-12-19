import requests
from endpoint.main_endpoint import MainEndpoint


class MethodGetAuthorize(MainEndpoint):

    def get_authorize(self, token):
        self.response = requests.get(f'{self.url}authorize/{token}', headers=self.headers)

        return self.response.status_code

    def get_authorize_negative(self, token):
        self.response = requests.get(f'{self.url}authorize/{token}1', headers=self.headers)

        return self.response.status_code
