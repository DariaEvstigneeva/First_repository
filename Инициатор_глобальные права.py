import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences_id = "https://{HOST}/api/audiences/2131/"
URL_audiences_copy = "https://{HOST}/api/audiences/2131/clone/"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates_id = "https://{HOST}/api/templates/email/376/"
URL_templates_copy = "https://{HOST}/api/templates/email/376/clone/"
URL_templates = "https://{HOST}/api/templates/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEyMjQ2ODgsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19lbXBzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0yMDc5NTUyOTY0IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19wcm9maWxlP21vZGU9dyZvcmdfb2lkPTEwMDAzMDA2NDggaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbnZ0cz9vcmdfb2lkPTEwMDAzMDA2NDgmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfY3R0cz9vcmdfb2lkPTEwMDAzMDA2NDgmbW9kZT13IiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiI5Y2Q4YTRkMy1mZjc2LTNlMWMtMDVhYi05ODFkODY0YmNhNmYiLCJ1cm46ZXNpYTpzYmpfaWQiOjIwNzk1NTI5NjQsImV4cCI6MTY4MTIyODI4OCwiaWF0IjoxNjgxMjI0Njg4LCJjbGllbnRfaWQiOiJQR1UifQ.kFI3Xrx0u6fSxOz1BMDy5LkEbr5uU2S8pUmbE8SH86RJJbld9DqpFURXdQHntIBAtuN215dDqRqUkfoZTUClcNRiqZ3a1TwWbOchST01MwssV7KSAQfOtVuXTKbco6nWw8lVgQeoaSgyRVRLy3giyFYN4-Qx5lDJGrH1I3847ctNsB5pIFN1eACaayN_4xhFza3vO0iriLV7vbzfYsStsmGFDbu6temk9vLOJyYd8HrK5Lad9VIyrs2994JecNS5g3SkUAaLNebaHotBPHr2OaH82dlGl3VPPQ7hwgq1QtsL2W0UgyE2yMXf6SoloB34W33e0NwQGlS7fBLS21u7AQ"

# успешное получение ца
response = requests.get(
    URL_audiences_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешное копирование ца
body = {
}

response = requests.post(
    URL_audiences_copy.format(HOST=HOST),
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

# успешное редактирование
body = {
    "description": "тест редактирования",
}

response = requests.put(
    URL_audiences_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

# удаление недоступно (Страница не найдена)
response = requests.delete(
    URL_audiences_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")
print("")

# успешное получение шаблона
response = requests.get(
    URL_templates_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешное копирование шаблона
body = {
}

response = requests.post(
    URL_templates_copy.format(HOST=HOST),
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

# успешное редактирование
body = {
    "description": "тест редактирования",
}

response = requests.put(
    URL_templates_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

# удаление недоступно (Страница не найдена)
response = requests.delete(
    URL_templates_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())