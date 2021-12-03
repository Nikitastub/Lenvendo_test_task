
def test_api(api):
    check_brand_list = []
    price_list = []
    response, sub_string = api.get_js_test_task()
    products = response['products']
    for product in products:
        assert sub_string in product['name']
        price_list.append(product['price'])
    # checking prices go from min to max
    assert price_list == sorted(price_list)
    # checking "name" include sub_string
    assert check_brand_list == []

