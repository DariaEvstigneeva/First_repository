import time


# тест на изменение последней ца
def test1_change_last_audience(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.audience.change_last_audience("Тест 12_12_2022", "Описание1")
    time.sleep(2)
    app.open_sidebar()
    time.sleep(1)
    app.session.logout()
    time.sleep(1)


# тест на изменение последней ца 2
def test2_change_last_audience(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.audience.change_last_audience2("Тест 12 12 2022", None)
    time.sleep(2)
    app.open_sidebar()
    time.sleep(1)
    app.session.logout()
    time.sleep(1)