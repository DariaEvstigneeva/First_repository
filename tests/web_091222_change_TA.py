import time


# тест на изменение последней ца
def test1_change_last_audience(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.audience.change_last_audience("Тест 09_12_22", "Описание")
    time.sleep(2)
    app.open_sidebar()
    time.sleep(1)
    app.session.logout()
    time.sleep(1)