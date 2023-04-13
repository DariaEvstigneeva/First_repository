import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
ID_audience = "2135"
audiences_updated_at = "2023-04-13T18:37:43.594492+03:00"
URL_audiences = "https://{HOST}/api/audiences/"
URL_audiences_id = "https://{HOST}/api/audiences/{ID_audience}/"
URL_audiences_copy = "https://{HOST}/api/audiences/{ID_audience}/clone/"
URL_audiences_update_status = "https://{HOST}/api/audiences/{ID_audience}/update-status/"

ID_selection_rule = "3886"
selection_rules_updated_at = "2023-04-13T18:37:43.575904+03:00"
URL_selection_rules = "https://{HOST}/api/selection-rules/"
URL_selection_rules_id = "https://{HOST}/api/selection-rules/{ID_selection_rule}/"

URL_audiences_test_query = "https://{HOST}/api/audiences/{ID_audience}/test-query/"
URL_audiences_contacts_archives = "https://{HOST}/api/audience-contacts-archives/"

ID_template = "371"
URL_templates = "https://{HOST}/api/templates/"
URL_templates_id = "https://{HOST}/api/templates/email/{ID_template}/"
URL_templates_copy = "https://{HOST}/api/templates/email/{ID_template}/clone/"
URL_templates_disable = "https://{HOST}/api/templates/email/{ID_template}/disable/"
URL_templates_deactivate = "https://{HOST}/api/templates/email/{ID_template}/deactivate/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0MDEyMDEsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5NzAzIGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfcHJvZmlsZT9vcmdfb2lkPTEwMDAyOTg5MjIgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbnZ0cz9vcmdfb2lkPTEwMDAyOTg5MjImbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfdmhscz9vcmdfb2lkPTEwMDAyOTg5MjImbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfZW1wcz9vcmdfb2lkPTEwMDAyOTg5MjImbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MTAwMDI5ODkyMiZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19jdHRzP29yZ19vaWQ9MTAwMDI5ODkyMiZtb2RlPXciLCJpc3MiOiJodHRwOlwvXC9lc2lhLWRlbW8udGVzdC5nb3N1c2x1Z2kucnVcLyIsInVybjplc2lhOnNpZCI6ImIyODllMmFiLWVjYTEtOTcwYi1iOWJmLWU4NWJjZWVkMjI4NyIsInVybjplc2lhOnNial9pZCI6MTAwMDI5OTcwMywiZXhwIjoxNjgxNDA0ODAxLCJpYXQiOjE2ODE0MDEyMDEsImNsaWVudF9pZCI6IlBHVSJ9.l067ygNJvTvsw95TSrP5YnRXdJOR3KDwAHS9xoVKpX6LNOzeAsAfnQgFUhvWaIGt6tz5MEjrFp3yPLRtZzgpsoBVTbqxm9a-jJLidQ97u7yKiS3TeR1btVLv9E3EPqO0v5H8Ffgu5bHc4ruYYJBWHwyCLmk97jk-Om99uXrS6-lMbfc_opW1LHVtnXi-iN1p0cgPkGJF2sEpQD0brgziWttw8XiTy1WS1htJq9dw50FpJM8Ko40C-T9qWlsqTFNMtEyHLb_5ao6dVGRa-MrIKmSLjqo6YGWwtCLwiSZ8Mdmf9VgMpc3Mjc_nyNdHqpvvrW6GKNLXRUC9n8M8lsiUZg"

# получение ца недоступно (Страница не найдена)
response = requests.get(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# копирование ца недоступно (Страница не найдена)
body = {
}

response = requests.post(
    URL_audiences_copy.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# поиск в перечне нужной ца (0)
response = requests.get(
    URL_audiences.format(HOST=HOST),
     headers={"Authorization":f"Bearer {token}"},
     params={"search":f"2124"},
)
pprint(response.json())

print("")

# редактирование ца недоступно (Страница не найдена)
body = {
    "description": "тест редактирования",
}

response = requests.put(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# перевод ца в статус черновик недоступно (У вас недостаточно прав для выполнения данного действия)
body = {
    "status": "DRAFT",
    "updated_at": audiences_updated_at
}

response = requests.patch(
    URL_audiences_update_status.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# удаление ца недоступно (Страница не найдена)
response = requests.delete(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# перевод ца в статус удалена недоступно (У вас недостаточно прав для выполнения данного действия)
body = {
    "status": "DELETED",
    "updated_at": audiences_updated_at
}

response = requests.patch(
    URL_audiences_update_status.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")
print("")

# поиск записей недоступен (Страница не найдена)
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

# выгрузка недоступна (У вас недостаточно прав для выполнения данного действия)
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

# получение выгрузок недоступно (У вас недостаточно прав для выполнения данного действия)
response = requests.get(
    URL_audiences_contacts_archives.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")
print("")

# получение правил недоступно (?)
response = requests.get(
    URL_selection_rules.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# получение правила недоступно (Страница не найдена)
response = requests.get(
    URL_selection_rules_id.format(HOST=HOST, ID_selection_rule=ID_selection_rule),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# создание правила недоступно (?)
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

# редактирование правила недоступно (Страница не найдена)
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

print("")

# деактивация правила недоступна (Страница не найдена)
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

# удаление правила недоступно (Страница не найдена)
response = requests.delete(
    URL_selection_rules_id.format(HOST=HOST, ID_selection_rule=ID_selection_rule),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")
print("")

# получение шаблона недоступно (Страница не найдена)
response = requests.get(
    URL_templates_id.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# копирование шаблона недоступно (Страница не найдена)
body = {
}

response = requests.post(
    URL_templates_copy.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# поиск в перечне нужного шаблона (0)
response = requests.get(
    URL_templates.format(HOST=HOST),
     headers={"Authorization":f"Bearer {token}"},
     params={"search":f"2124"},
)
pprint(response.json())

print("")

# редактирование шаблона недоступно (У вас недостаточно прав для выполнения данного действия)
body = {
    "description": "тест редактирования",
}

response = requests.put(
    URL_templates_id.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())


print("")

# перевод шаблона в статус черновик недоступен (У вас недостаточно прав для выполнения данного действия)
body = {
}

response = requests.put(
    URL_templates_deactivate.format(HOST=HOST,ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# удаление шаблона недоступно (У вас недостаточно прав для выполнения данного действия)
response = requests.delete(
    URL_templates_id.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# перевод шаблона в статус удалена недоступно (У вас недостаточно прав для выполнения данного действия)
body = {
}

response = requests.put(
    URL_templates_disable.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())