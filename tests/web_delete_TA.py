import time


# тест на удаление последней ца
def test1_delete_last_audience(app):
    time.sleep(1)
    if app.audience.count() == 26:
        time.sleep(1)
        app.audience.create("13_12_2022 11", "1312")
    app.audience.delete_last_audience()
    time.sleep(1)
