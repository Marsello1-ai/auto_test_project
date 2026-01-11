class MainEndpoint:
    url = 'http://memesapi.course.qa-practice.com/'
    headers = {'Content-Type': 'application/json'}
    response = None
    token_id = None
    payload = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    def check_negative_status_code_is_400(self):
        assert self.response.status_code == 400

    def check_negative_status_code_is_401(self):
        assert self.response.status_code == 401

    def check_negative_status_code_is_403(self):
        assert self.response.status_code == 403

    def check_negative_status_code_is_404(self):
        assert self.response.status_code == 404

    def check_negative_status_code_is_405(self):
        assert self.response.status_code == 405

    def check_payload_meme(self, check_id=False):
        body = self.response.json()
        if check_id:
            # Проверяем, что id в ответе совпадает с id в ожидаемом payload
            assert body["id"] == self.payload["id"]
        assert body["text"] == self.payload["text"]
        assert body["url"] == self.payload["url"]
        assert body["tags"] == self.payload["tags"]
        assert body["info"] == self.payload["info"]
