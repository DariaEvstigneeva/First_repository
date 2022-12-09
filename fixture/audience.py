from selenium.webdriver.common.by import By
import time

class Work_with_audiences:

    def __init__(self, app):
        self.app = app

    # создание ЦА
    # нужно добавить также добавление тегов
    # создать отдельные методы с деактивацией чекбокса, со сменой режима, добавление правил
    def create(self, name_audience, description_audience):
        element = self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained")
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
        time.sleep(1)
        self.app.driver.find_element(By.ID, "name").click()
        self.app.driver.find_element(By.ID, "name").send_keys(name_audience)
        time.sleep(1)
        self.app.driver.find_element(By.ID, "description").click()
        self.app.driver.find_element(By.ID, "description").send_keys(description_audience)
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()