import time


# тест на добавление РС (с именем и описанием)
def test1_create_mailing_lists(app):
    app.link_acrm()
    app.session.login("devstigneeva", "fWd9iGZz")
    time.sleep(2)
    app.module_mailing_lists()
    time.sleep(2)
    app.mailing_list.create("121222", "1212")
    # нужна проверка, что выполнен переход на страницу к перечню рс
    time.sleep(2)
    app.open_sidebar()
    time.sleep(2)
    app.session.logout()
    time.sleep(2)