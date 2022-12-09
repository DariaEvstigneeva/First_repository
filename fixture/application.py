from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fixture.session import WorkSession

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = WorkSession(self)

    def destroy(self):
        self.driver.quit()

    # открытие боковой панели с данными пользователя
    def open_sidebar(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.CSS_SELECTOR, ".user-menu-module__user-name-text__2_L8L")
        self.driver.find_element(By.CSS_SELECTOR, ".user-menu-module__user-name-text__2_L8L").click()

    # создание ЦА
    # нужно добавить также добавление тегов
    # создать отдельные методы с деактивацией чекбокса, со сменой режима, добавление правил
    def create_audiences(self, name_audience, description_audience):
        element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained")
        self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys(name_audience)
        time.sleep(1)
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys(description_audience)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()

    # настройки браузера и ссылки
    def link_acrm(self):
        self.driver.get("https://armcrm-dev.test.gosuslugi.ru/login")
        self.driver.set_window_size(1920, 1080)