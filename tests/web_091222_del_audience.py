import time


# тест на удаление последней ца
def test1_delete_last_audience(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    #вносим изменения тут
    app.audience.delete_last_audience()
    time.sleep(2)
    app.open_sidebar()
    time.sleep(2)
    app.session.logout()
    time.sleep(2)