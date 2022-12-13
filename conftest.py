# Фикстуры необходимы для структурирования тестового кода.
# Функция fixture запускается перед тестами, которые ее используют.
# для совместного использования фикстур в нескольких тестовых файлах лучше использовать файл conftest.py
# файл должен находиться где-то в общем месте, централизованно для всех тестов.
# Хотя conftest.py является модулем Python, он не должен импортироваться тестовыми файлами.


import pytest
from fixture.application import Application

fixture = None


#фикстура
# инициализация фикстуры
@pytest.fixture
# Декоратор @pytest.fixture() используется, чтобы сообщить pytest, что функция является фикстурой.
# при запуске всех тестов, чтобы все тесты выполнялись в одном браузер в скобки вписать scope="session"
def app(request): # имя фикстуры
    # когда указывается имя фикстуры в списке параметров тестовой функции, pytest знает, как запустить её перед запуском теста.
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login("devstigneeva", "fWd9iGZz")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login("devstigneeva", "fWd9iGZz")
    return fixture

    # финализация фикстуры
    # для выполнения все в одной сессии
    # чтобы фикстура сработала, ее нужно явно где-то указать или указать свойство autouse=True, которое поддерживает pytest
@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture