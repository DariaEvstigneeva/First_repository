import time


# тест на добавление ца (с именем и описанием)
def test1_create_audience(app):
    time.sleep(2)
    app.audience.create("131222", "1312")
    # нужна проверка, что выполнен переход на страницу к перечню ца
    time.sleep(2)


def test2_create_audience(app):
    time.sleep(2)
    app.audience.create("13_12_22", "13_12")
    # нужна проверка, что выполнен переход на страницу к перечню ца
    time.sleep(2)