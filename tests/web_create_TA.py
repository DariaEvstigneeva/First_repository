import time


# тест на добавление ца (с именем и описанием)
def test1_create_audience(app):
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.audience.create("131222", "1312")
    # нужна проверка, что выполнен переход на страницу к перечню ца
    time.sleep(2)
    app.session.logout()
    time.sleep(2)
