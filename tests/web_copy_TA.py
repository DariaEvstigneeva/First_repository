import time


# тест на копирование последней ца
def test1_copy_last_audience(app):
    time.sleep(1)
    app.audience.copy_last_audience()
    time.sleep(1)