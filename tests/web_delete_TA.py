import time


# тест на удаление последней ца
def test1_delete_last_audience(app):
    time.sleep(1)
    app.audience.delete_last_audience()
    time.sleep(1)
