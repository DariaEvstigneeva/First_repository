from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class Work_with_audiences:

    def __init__(self, app):
        self.app = app

    # создание ЦА
    # нужно добавить также добавление тегов
    # создать отдельные методы с деактивацией чекбокса, со сменой режима, добавление правил
    def create(self, name_audience, description_audience):
        self.app.default_page()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained").click()
        time.sleep(1)
        self.app.driver.find_element(By.ID, "name").click()
        self.app.driver.find_element(By.ID, "name").send_keys(name_audience)
        time.sleep(1)
        self.app.driver.find_element(By.ID, "description").click()
        self.app.driver.find_element(By.ID, "description").send_keys(description_audience)
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()

    #удаление последней ЦА
    def delete_last_audience(self):
        self.app.default_page()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(1) .MuiButtonBase-root:nth-child(3) > svg").click()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedError").click()


    # копирование последней ЦА
    def copy_last_audience(self):
        self.app.default_page()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR,".MuiTableRow-root:nth-child(1) .MuiButtonBase-root:nth-child(2) > svg").click()
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()

    # изменение последней ЦА
    def change_last_audience(self, name_audience, description_audience):
        self.app.default_page()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR,".MuiTableRow-root:nth-child(1) .styles__actions-icons__2Yqi9 > .MuiButtonBase-root:nth-child(1) path").click()
        time.sleep(1)
        self.app.driver.find_element(By.ID, "name").send_keys(Keys.CONTROL + "a")
        self.app.driver.find_element(By.ID, "name").send_keys(Keys.DELETE)
        self.app.driver.find_element(By.ID, "name").send_keys(name_audience)
        time.sleep(1)
        self.app.driver.find_element(By.ID, "description").send_keys(Keys.CONTROL + "a")
        self.app.driver.find_element(By.ID, "description").send_keys(Keys.DELETE)
        self.app.driver.find_element(By.ID, "description").send_keys(description_audience)
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()

    # изменение последней ЦА 2
    def change_last_audience2(self, name_audience, description_audience):
        self.app.default_page()
        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR,".MuiTableRow-root:nth-child(1) .styles__actions-icons__2Yqi9 > .MuiButtonBase-root:nth-child(1) path").click()
        time.sleep(1)
        self.type("name", name_audience)
        self.type("description", description_audience)
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root:nth-child(3)").click()

    def type(self, field_id, text):
        if text is not None:
            self.app.driver.find_element(By.ID, field_id).send_keys(Keys.CONTROL + "a")
            self.app.driver.find_element(By.ID, field_id).send_keys(Keys.DELETE)
            self.app.driver.find_element(By.ID, field_id).send_keys(text)


    # получение списка ЦА
    def get_audience_list(self):
        audience_list = []
        for element in self.app.driver.find_elements(By.CSS_SELECTOR, ".Mui TableCell-alignLeft"):
            text = element.text
            audience_list.append(text)
        return audience_list
    # def __repr__(self):
    #    return "%s:%s" % (self.name_audience)
    # def __eq__(self, other):
    #    return self.name == other.name

    # количество элементов на странице - не работает
    # def count(self):
    #     return len(self.app.driver.find_element(By.ID, "name"))

    # количество элементов на странице - не понятный
    # def count(self):
    #    return self.app.driver.find_elements(By.CSS_SELECTOR, "div.styles__tags-wrapper__273zE")