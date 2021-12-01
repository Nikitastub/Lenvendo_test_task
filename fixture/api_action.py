import requests

def get_response(search='Huawei', sort_field='price'):
    req = requests.get("https://www.lenvendo.ru/api/js-test-task/?search={}&sort_field={}".format(search, sort_field))
    res = req.json()
    products = res['products']
    sub_string = search
    return (products, sub_string)
