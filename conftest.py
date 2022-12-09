import pytest
from fixture.application import Application


#фикстура
@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture