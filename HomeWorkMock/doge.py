import requests


# Калсс содержит вызовы методов api сервиса, серилезовнные в методы класса
class Doge:
    base_url = "https://dog.ceo/api"

    def all_breeds(self):
        response = requests.get(f"{self.base_url}/breeds/list/all").json()
        print(response)
        if response.ok:
            return response
        else:
            return None

    def random_images(self, num):
        response = requests.get(f"{self.base_url}/breeds/image/random/{num}").json()
        print(response)
        if response.ok:
            return response
        else:
            return None

    def get_random(self):
        response = requests.get(f"{self.base_url}/breeds/image/random")
        print(response)
        if response.ok:
            return response
        else:
            return None

    def sub_breeds(self, name):
        response = requests.get(f"{self.base_url}/breed/{name}/list").json()
        print(response)
        if response.ok:
            return response
        else:
            return None
