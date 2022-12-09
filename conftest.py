import pytest
from fixture.application import Application


#фикстура
@pytest.fixture()
# при запуске всех тестов, чтобы все тесты выполнялись в одном браузер в скобки вписать scope="session"
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture