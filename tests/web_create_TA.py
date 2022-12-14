import time


# тест на добавление ца (с именем и описанием)
def test1_create_audience(app):
    time.sleep(1)
    old_audiences = app.audience.get_audience_list()
    # получение старого списка ЦА (до добавления ЦА)
    app.audience.create("Test_1", "description")
    time.sleep(1)
    new_audiences = app.audience.get_audience_list()
    # получение нового списка ЦА (после добавления ЦА), проверить можно через дебаг
    assert len(old_audiences) == len(new_audiences) # сравнение размера списка
    time.sleep(1)


def test2_create_audience(app):
    time.sleep(1)
    app.audience.create("Test_2", "description")
    time.sleep(1)
    app.default_page()
    time.sleep(1)