import pytest
from fixture.application import Application

fixture = None

@pytest.fixture(scope='session')
def app(request):
    global fixture
    if fixture is None:
        fixture = Application(base_url='http://qa.digift.ru/')
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

