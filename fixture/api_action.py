import requests

class ApiActionHelper:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_js_test_task(self, payload=None):
        price_list = []
        url = self.base_url + 'js-test-task/'
        request = requests.get(url=url, params=payload)
        response = request.json()
        if '200' in str(request):
            if payload is not None:
                if 'search' in payload:
                    sub_string = payload['search']
                    for product in response['products']:
                        assert sub_string in product['name']
                if ('sort_field', 'price') in payload.items():
                    for product in response['products']:
                        price_list.append(product['price'])
                    assert price_list == sorted(price_list)
        else:
            raise BaseException('Bad request: {}.\nResponse body: {}'.format(request, response))

