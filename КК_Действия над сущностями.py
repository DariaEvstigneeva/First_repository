import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
ID_audience = "2131"
audiences_updated_at = "2023-04-10T10:54:30.656413+03:00"
URL_audiences = "https://{HOST}/api/audiences/"
URL_audiences_id = "https://{HOST}/api/audiences/{ID_audience}/"
URL_audiences_copy = "https://{HOST}/api/audiences/{ID_audience}/clone/"
URL_audiences_update_status = "https://{HOST}/api/audiences/{ID_audience}/update-status/"

ID_template = "377"
URL_templates = "https://{HOST}/api/templates/"
URL_templates_id = "https://{HOST}/api/templates/email/{ID_template}/"
URL_templates_copy = "https://{HOST}/api/templates/email/{ID_template}/clone/"
URL_templates_disable = "https://{HOST}/api/templates/email/{ID_template}/disable/"
URL_templates_deactivate = "https://{HOST}/api/templates/email/{ID_template}/deactivate/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEyMjQ2ODgsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19lbXBzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0yMDc5NTUyOTY0IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19wcm9maWxlP21vZGU9dyZvcmdfb2lkPTEwMDAzMDA2NDggaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbnZ0cz9vcmdfb2lkPTEwMDAzMDA2NDgmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfY3R0cz9vcmdfb2lkPTEwMDAzMDA2NDgmbW9kZT13IiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiI5Y2Q4YTRkMy1mZjc2LTNlMWMtMDVhYi05ODFkODY0YmNhNmYiLCJ1cm46ZXNpYTpzYmpfaWQiOjIwNzk1NTI5NjQsImV4cCI6MTY4MTIyODI4OCwiaWF0IjoxNjgxMjI0Njg4LCJjbGllbnRfaWQiOiJQR1UifQ.kFI3Xrx0u6fSxOz1BMDy5LkEbr5uU2S8pUmbE8SH86RJJbld9DqpFURXdQHntIBAtuN215dDqRqUkfoZTUClcNRiqZ3a1TwWbOchST01MwssV7KSAQfOtVuXTKbco6nWw8lVgQeoaSgyRVRLy3giyFYN4-Qx5lDJGrH1I3847ctNsB5pIFN1eACaayN_4xhFza3vO0iriLV7vbzfYsStsmGFDbu6temk9vLOJyYd8HrK5Lad9VIyrs2994JecNS5g3SkUAaLNebaHotBPHr2OaH82dlGl3VPPQ7hwgq1QtsL2W0UgyE2yMXf6SoloB34W33e0NwQGlS7fBLS21u7AQ"

# успешное получение ца
response = requests.get(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# копирование ца недоступно
body = {
}

response = requests.post(
    URL_audiences_copy.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# поиск в перечне нужной ца
response = requests.get(
    URL_audiences.format(HOST=HOST),
     headers={"Authorization":f"Bearer {token}"},
     params={"search":f"2124"},
)
pprint(response.json())

print("")

# редактирование ца недоступно
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

# перевод ца в статус черновик недоступно
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

# удаление ца недоступно
response = requests.delete(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# перевод ца в статус удалена недоступно
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

# успешное получение шаблона
response = requests.get(
    URL_templates_id.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешное копирование шаблона
body = {
}

response = requests.post(
    URL_templates_copy.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# поиск в перечне нужного шаблона
response = requests.get(
    URL_templates.format(HOST=HOST),
     headers={"Authorization":f"Bearer {token}"},
     params={"search":f"376"},
)
pprint(response.json())

print("")

# успешное редактирование шаблона
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

# успешный перевод шаблона в статус черновик
body = {
}

response = requests.put(
    URL_templates_deactivate.format(HOST=HOST,ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response)

print("")

# успешное удаление шаблона (только если автор, исключение - глобальный доступ)
response = requests.delete(
    URL_templates_id.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешный перевод шаблона в статус удален (только если автор, для глобального доступа недоступно)
body = {
}

response = requests.put(
    URL_templates_disable.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())