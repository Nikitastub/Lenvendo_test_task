import pytest

@pytest.mark.parametrize(('search', 'sort_field'), [('Huawei', 'price')])
def test_api(api, search, sort_field):
    api.get_js_test_task(search=search, sort_field=sort_field)