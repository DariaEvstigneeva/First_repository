import time


# тест на изменение последней ца
def test1_change_last_audience(app):
    time.sleep(1)
    app.audience.change_last_audience("Тест 13_12_2022", "Описание1")
    time.sleep(1)



# тест на изменение последней ца 2
def test2_change_last_audience(app):
    time.sleep(1)
    app.audience.change_last_audience2("Тест 13 12 2022", None)
    time.sleep(1)
