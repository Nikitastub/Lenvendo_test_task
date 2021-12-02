import requests

class ApiActionHelper:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self):
        payload = {'search': 'Huawei', 'sort_field': 'price'}
        response = ((requests.get(url=self.base_url, params=payload)).json())
        sub_string = payload['search']
        return response, sub_string


