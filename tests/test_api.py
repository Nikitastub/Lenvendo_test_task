
def test_api(api):
    price_list = []
    response, sub_string = api.get_js_test_task({'search': 'Huawei', 'sort_field': 'price'})
    products = response['products']
    for product in products:
        # checking "name" include sub_string
        assert sub_string in product['name']
        price_list.append(product['price'])
    # checking prices go from min to max
    assert price_list == sorted(price_list)

