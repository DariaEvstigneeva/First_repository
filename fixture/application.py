from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import WorkSession
from fixture.audience import Work_with_audiences
from fixture.mailing_list import Work_with_mailing_lists

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = WorkSession(self)
        self.audience = Work_with_audiences(self)
        self.mailing_list = Work_with_mailing_lists(self)

    def destroy(self):
        self.driver.quit()

    def is_valid(self): #блок с перехватом исключения
        try:
            self.driver.current_url
            return True
        except:
            return False

    # открытие боковой панели с данными пользователя
    def open_sidebar(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".user-menu-module__user-name-text__2_L8L").click()

    # настройки браузера и ссылки
    def link_acrm(self):
        self.driver.get("https://armcrm-dev.test.gosuslugi.ru/login")
        # Метод driver.get перенаправляет к странице URL в параметре.
        # WebDriver будет ждать пока страница не загрузится полностью
        self.driver.set_window_size(1920, 1080)

    # переход в раздел РС
    def module_mailing_lists(self):
        self.driver.find_element(By.CSS_SELECTOR, ".styles__link__lDjnp:nth-child(2) .MuiTypography-root").click()