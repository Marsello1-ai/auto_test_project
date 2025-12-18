class MainEndpoint:
    url = 'http://memesapi.course.qa-practice.com/'
    headers = {'Content-Type': 'application/json'}
    response = None
    token_id = None

    def check_status_code(self):
        assert self.response.status_code == 200
