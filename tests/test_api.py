import pytest



@pytest.mark.parametrize('payload', [{'search': 'Huawei', 'sort_field': 'price'}, {'search': 'Huawei'},
                                      {'sort_field': 'price'}, None])
def test_api(api, payload):
    api.get_js_test_task(payload)