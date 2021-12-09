import requests

class ApiActionHelper:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_js_test_task(self, search=None, sort_field = None):
        payload = {'search': search, 'sort_field': sort_field}
        price_list = []
        url = self.base_url + 'js-test-task/'
        request = requests.get(url=url, params=payload)
        response = request.json()
        if '200' in str(request):
            if search is not None:
                sub_string = payload['search']
                for product in response['products']:
                    assert sub_string in product['name'],\
                        "There is no substring '{}' in product's name: '{}'".format(sub_string, product['name'])
            if sort_field == 'price':
                for product in response['products']:
                    price_list.append(product['price'])
                assert price_list == sorted(price_list), "The products are not sorted by price"
        else:
            raise BaseException('Bad request: {}.\nResponse body: {}'.format(request, response))

