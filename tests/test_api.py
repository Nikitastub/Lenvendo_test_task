
def test_api(api):
    price_list = []
    payload = {'search':'Huawei', 'sort_field':'price'}
    response, sub_string = api.get_js_test_task(payload)
    products = response['products']
    if (sub_string is not None):
        for product in products:
            assert sub_string in product['name']
    if ('sort_field', 'price') in payload.items():
        for product in products:
            price_list.append(product['price'])
        assert price_list == sorted(price_list)