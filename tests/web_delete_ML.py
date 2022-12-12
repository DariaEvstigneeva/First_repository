import time


# тест на удаление последней ца
def test1_delete_last_mailing_list(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.module_mailing_lists()
    time.sleep(2)
    app.mailing_list.delete_last_mailing_list()
    time.sleep(2)
    app.open_sidebar()
    time.sleep(1)
    app.session.logout()
    time.sleep(1)