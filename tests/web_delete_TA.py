import time
from random import random

# тест на удаление последней ца
def test1_delete_last_audience(app):
    time.sleep(1)
    app.audience.delete_last_audience()
    time.sleep(1)



    #time.sleep(1)
    #old_audiences = app.audience.get_audience_list() локальная переменная
    #app.audience.delete_last_audience()
    #time.sleep(1)
    #new_audiences = app.audience.get_audience_list()
    #old_audiences[0:1] = []
    #assert old_audiences == new_audiences
    #time.sleep(1)