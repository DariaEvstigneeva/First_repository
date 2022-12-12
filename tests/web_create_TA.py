import time


# тест на добавление ца (с именем и описанием)
def test1_create_audience(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.audience.create("121222", "1212")
    # нужна проверка, что выполнен переход на страницу к перечню ца
    time.sleep(2)
    app.open_sidebar()
    time.sleep(2)
    app.session.logout()
    time.sleep(2)
