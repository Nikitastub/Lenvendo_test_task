
def test_api(api):
    check_brand_list = []
    price_list = []
    response, sub_string = api.get()
    products = response['products']
    for product in products:
        if product['name'].find(sub_string) < 1:
            check_brand_list.append('-')
        price_list.append(product['price'])
    # checking prices go from min to max
    assert price_list == sorted(price_list)
    # checking "name" include sub_string
    assert check_brand_list == []

