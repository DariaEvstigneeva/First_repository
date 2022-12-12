from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class Work_with_mailing_lists:

    def __init__(self, app):
        self.app = app

    # создание РС
    def create(self, name_mailing_lists, description_mailing_lists):
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
        time.sleep(1)
        self.app.driver.find_element(By.ID, "name").click()
        self.app.driver.find_element(By.ID, "name").send_keys(name_mailing_lists)
        time.sleep(1)
        self.app.driver.find_element(By.ID, "description").click()
        self.app.driver.find_element(By.ID, "description").send_keys(description_mailing_lists)
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()

    #удаление последнего РС
    def delete_last_mailing_lists(self):
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(1) .MuiButtonBase-root:nth-child(3) > svg").click()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedError").click()

    # копирование последнего РС
    def copy_last_mailing_lists(self):
        self.app.driver.find_element(By.CSS_SELECTOR,".MuiTableRow-root:nth-child(1) .MuiButtonBase-root:nth-child(2) > svg").click()
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()

    # изменение последнего РС
    def change_last_mailing_lists(self, name_mailing_lists, description_mailing_lists):
        self.app.driver.find_element(By.CSS_SELECTOR,".MuiTableRow-root:nth-child(1) .styles__actions-icons__2Yqi9 > .MuiButtonBase-root:nth-child(1) path").click()
        time.sleep(1)
        self.app.driver.find_element(By.ID, "name").send_keys(Keys.CONTROL + "a")
        self.app.driver.find_element(By.ID, "name").send_keys(Keys.DELETE)
        self.app.driver.find_element(By.ID, "name").send_keys(name_mailing_lists)
        time.sleep(1)
        self.app.driver.find_element(By.ID, "description").send_keys(Keys.CONTROL + "a")
        self.app.driver.find_element(By.ID, "description").send_keys(Keys.DELETE)
        self.app.driver.find_element(By.ID, "description").send_keys(description_mailing_lists)
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()