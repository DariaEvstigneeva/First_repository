import requests
from pprint import pprint
import json

HOST = "armcrm-dev.test.gosuslugi.ru"
ID_audience = "2135"

ID_selection_rule = "3886"
selection_rules_updated_at = "2023-04-13T18:22:52.969797+03:00"
URL_selection_rules = "https://{HOST}/api/selection-rules/"
URL_selection_rules_id = "https://{HOST}/api/selection-rules/{ID_selection_rule}/"

URL_audiences_test_query = "https://{HOST}/api/audiences/{ID_audience}/test-query/"
URL_audiences_contacts_archives = "https://{HOST}/api/audience-contacts-archives/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEzOTYyMDcsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2VtcHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_bW9kZT13Jm9yZ19vaWQ9MjA3OTU1MTc5NSBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5MjgyIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiI5MDAyYjYxNC1jZDUwLWMzNzItM2JhNy1hMDhhZDBmOGU4ZmQiLCJ1cm46ZXNpYTpzYmpfaWQiOjEwMDAyOTkyODIsImV4cCI6MTY4MTM5OTgwNywiaWF0IjoxNjgxMzk2MjA3LCJjbGllbnRfaWQiOiJQR1UifQ.TzNJn0lg9Bp7bsvFtNyQ3Lj8qfKUh3ddGBD6u7Ic3RKJtc-uUypileoEmNo_Uy1SyKKzBzQaKhmZ6eSkYxAB14Gww1nDisRXxOfxDk4mygCDG3sQLkVKreSIOtoW9LnqNofXWSNT6YDNi1_TrxZsRZKb62DZb_4By4-yy0LO-G-GEAJU73amEVhfmiiTSnI8ESzL4e53eoNkkL3EhSxQWhYFfCVYc9A8qDv-8NYq3texeTMihuk-wlzmZBPUlM1xvnXweg1ZyYtqOZkRDU5pDXL0gznFpWjbgTBkIEpDpR_ila72FgQv3O1M-mIqtBzlnbDXsrUznPw_oC1Kqsjqqg"



# успешный поиск записей без примера найденных записей
# успешный поиск записей с примером найденных записей
# поиск записей недоступен
body = {
}

response = requests.post(
    URL_audiences_test_query.format(HOST=HOST,ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")
print("")
print("")

# успешная выгрузка
# выгрузка недоступна
body = {"audience_id": {ID_audience},
        "query_params": [{"limit": 1, "random_ordering": True}]
}

response = requests.post(
    URL_audiences_contacts_archives.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")
print("")
print("")

# успешное получение выгрузок
# получение выгрузок недоступно
response = requests.get(
    URL_audiences_contacts_archives.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())


print("")
print("")
print("")

# успешное получение правил
# получение правил недоступно
response = requests.get(
    URL_selection_rules.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")
print("")
print("")

# успешное получение правила
# получение правила недоступно
response = requests.get(
    URL_selection_rules_id.format(HOST=HOST, ID_selection_rule=ID_selection_rule),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешное создание правила
# создание правила недоступно
body = {
    "name": "ML",
    "status": "ACTIVE",
    "audience": {ID_audience},
    "mailing_lists": [1217]
}

response = requests.post(
    URL_selection_rules.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")
print("")
print("")

# успешное редактирование правила
# редактирование правила недоступно
body = {
    "name": "ML0",
    "status": "ACTIVE",
    "audience": {ID_audience},
    "mailing_lists": [1217],
    "updated_at": selection_rules_updated_at
}

response = requests.put(
    URL_selection_rules_id.format(HOST=HOST, ID_selection_rule=ID_selection_rule),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

# успешная деактивация правила
# деактивация правила недоступна
body = {
    "status": "DISABLED",
    "updated_at": selection_rules_updated_at
}

response = requests.patch(
    URL_selection_rules_id.format(HOST=HOST, ID_selection_rule=ID_selection_rule),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# успешное удаление правила
# удаление правила недоступно
response = requests.delete(
    URL_selection_rules_id.format(HOST=HOST, ID_selection_rule=ID_selection_rule),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")