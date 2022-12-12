import time


# тест на изменение последней ца
def test1_change_last_mailing_list(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.module_mailing_lists()
    time.sleep(2)
    app.mailing_list.change_last_mailing_list("Тест 12_12_22", "Описание")
    time.sleep(2)
    app.open_sidebar()
    time.sleep(1)
    app.session.logout()
    time.sleep(1)