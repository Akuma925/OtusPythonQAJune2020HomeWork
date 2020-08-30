import requests


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """

    def __init__(self, base_address, status_code):
        self.base_address = base_address
        self.status_code = int(status_code)

    def create_session(self):
        return requests.Session()

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers, verify=False)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params, verify=False)





