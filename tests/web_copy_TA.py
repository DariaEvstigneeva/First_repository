import time


# тест на копирование последней ца
def test1_copy_last_audience(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.audience.copy_last_audience()
    time.sleep(2)
    app.open_sidebar()
    time.sleep(1)
    app.session.logout()
    time.sleep(1)