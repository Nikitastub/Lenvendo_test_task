import pytest
from fixture.application import Application
from fixture.api_action import ApiActionHelper
import jsonpickle
import os.path

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

@pytest.fixture()
def api():
    apifixture = ApiActionHelper(base_url='https://www.lenvendo.ru/api/js-test-task/')
    return apifixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data"):
            testdata = load_from_json(fixture)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\{}.json".format(file))) as f:
        return jsonpickle.decode(f.read())

