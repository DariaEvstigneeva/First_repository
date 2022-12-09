from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fixture.session import WorkSession
from fixture.audience import Work_with_audiences

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = WorkSession(self)
        self.audience = Work_with_audiences(self)

    def destroy(self):
        self.driver.quit()

    # открытие боковой панели с данными пользователя
    def open_sidebar(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.CSS_SELECTOR, ".user-menu-module__user-name-text__2_L8L")
        self.driver.find_element(By.CSS_SELECTOR, ".user-menu-module__user-name-text__2_L8L").click()

    # настройки браузера и ссылки
    def link_acrm(self):
        self.driver.get("https://armcrm-dev.test.gosuslugi.ru/login")
        self.driver.set_window_size(1920, 1080)