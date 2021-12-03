import requests

class ApiActionHelper:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_js_test_task(self, payload):
        # payload = {'search': 'Huawei', 'sort_field': 'price'}
        url = self.base_url + 'js-test-task/'
        response = ((requests.get(url=url, params=payload)).json())
        sub_string = payload['search']
        return response, sub_string


