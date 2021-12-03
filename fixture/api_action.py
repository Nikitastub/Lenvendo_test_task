import requests

class ApiActionHelper:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_js_test_task(self, payload=None):
        url = self.base_url + 'js-test-task/'
        req = requests.get(url=url, params=payload)
        assert '200' in str(req)
        res = req.json()
        if payload is not None:
            sub_string = list(payload.values())[0]
            return res, sub_string
        else:
            return res, None


