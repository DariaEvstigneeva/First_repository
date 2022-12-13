# для совместного использования фикстур в нескольких тестовых файлах лучше использовать файл conftest.py
# файл должен находиться где-то в общем месте, централизованно для всех тестов.
# Хотя conftest.py является модулем Python, он не должен импортироваться тестовыми файлами.
# Фикстуры необходимы для структурирования тестового кода.
# Функция fixture запускается перед тестами, которые ее используют.



import pytest
from fixture.application import Application


#фикстура
@pytest.fixture(scope = "session")
# Декоратор @pytest.fixture() используется, чтобы сообщить pytest, что функция является фикстурой.
# при запуске всех тестов, чтобы все тесты выполнялись в одном браузер в скобки вписать scope="session"
def app(request): # имя фикстуры
    # когда указывается имя фикстуры в списке параметров тестовой функции, pytest знает, как запустить её перед запуском теста.
    fixture = Application()
    fixture.session.login("devstigneeva", "fWd9iGZz")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture