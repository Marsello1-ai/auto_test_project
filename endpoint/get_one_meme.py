import requests
from endpoint.main_endpoint import MainEndpoint
import allure


class MethodGetOneMeme(MainEndpoint):
    meme_id = None

    @allure.title('Показываем 1 мем')
    def get_one_meme(self, meme_id, token_id):
        with allure.step('Создаем мем и отдаем его meme_id'):
            headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.meme_id = meme_id

        with allure.step('Дергаем запрос на просмотр созданного мема'):
            self.response = requests.get(f'{self.url}meme/{meme_id}', headers=headers)

        with allure.step('Отдаем тело ответа и удаляем мем'):
            return self.response

    def get_one_meme_negative_meme_id(self, token_id):
        headers = {'Content-Type': 'application/json', 'Authorization': token_id}
        self.response = requests.get(f'{self.url}meme/', headers=headers)

        return self.response

    def get_one_meme_negative_authorize(self, meme_id):
        headers = {'Content-Type': 'application/json', 'Authorization': None}
        self.response = requests.get(f'{self.url}meme/{meme_id}', headers=headers)

        return self.response

    def check_meme_id_in_payload(self):
        assert self.response.json()["id"] == self.meme_id
