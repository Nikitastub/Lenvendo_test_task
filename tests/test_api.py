
def test_api(api):
    price_list = []
    payload = {'search':'Huawei', 'sort_field':'price'}
    response, sub_string = api.get_js_test_task(payload)
    products = response['products']
    if sub_string is not None:
        for product in products:
            # checking "name" include sub_string
            assert sub_string in product['name']
            price_list.append(product['price'])
        # checking prices go from min to max
        assert price_list == sorted(price_list)
    else:
        raise ValueError('запрос не содержит параметра для фильтрации')
