from fixture import api_action

def test_api():
    check_brand_list = []
    price_list = []
    products, sub_string = api_action.get_response()
    # sub_string = api_action.get_response()[1]
    for product in products:
        if product['name'].find(sub_string) < 1:
            check_brand_list.append('-')
        price_list.append(product['price'])
    assert price_list == sorted(price_list)
    assert check_brand_list == []

