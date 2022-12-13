from selenium.webdriver.common.by import By
import time

class WorkSession:

    def __init__(self, app):
        self.app = app

    # авторизация
    def login(self, username, password):
        self.app.link_acrm()
        self.app.driver.find_element(By.ID, "username").send_keys(username)
        self.app.driver.find_element(By.ID, "password").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, ".styles__button__2b5Jq").click()

    # выход из системы
    def logout(self):
        self.app.open_sidebar()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR, ".user-menu-module__user-info-role-button__3I6l_").click()

