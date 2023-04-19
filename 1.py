import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
ID_audience = "2178"
audiences_updated_at = "2023-04-14T19:15:25.185123+03:00"
URL_audiences = "https://{HOST}/api/audiences/"
URL_audiences_id = "https://{HOST}/api/audiences/{ID_audience}/"
URL_audiences_copy = "https://{HOST}/api/audiences/{ID_audience}/clone/"
URL_audiences_update_status = "https://{HOST}/api/audiences/{ID_audience}/update-status/"

ID_template = "200"
URL_templates = "https://{HOST}/api/templates/"
URL_templates_id = "https://{HOST}/api/templates/email/{ID_template}/"
URL_templates_copy = "https://{HOST}/api/templates/email/{ID_template}/clone/"
URL_templates_disable = "https://{HOST}/api/templates/email/{ID_template}/disable/"
URL_templates_deactivate = "https://{HOST}/api/templates/email/{ID_template}/deactivate/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE3MjEwMDMsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0yMDc5NTUxNzYxIGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfZW1wcz9vcmdfb2lkPTIwNzk1NTI5NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19jdHRzP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbnZ0cz9vcmdfb2lkPTIwNzk1NTI5NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfcHJvZmlsZT9tb2RlPXcmb3JnX29pZD0yMDc5NTUyOTQzIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiIyMzIyN2UwYS04YWY4LWIyM2ItNTFlNS02YzJhNDhkNDY4YjIiLCJ1cm46ZXNpYTpzYmpfaWQiOjIwNzk1NTE3NjEsImV4cCI6MTY4MTcyNDYwMywiaWF0IjoxNjgxNzIxMDAzLCJjbGllbnRfaWQiOiJQR1UifQ.aV_oKwIVho66qkXv9rvlAB1EDHAGGVc-BdCV-G4LE-Xx-CrA9CTO9UlST4PKqnkUIi8Jr4eM20TblvYDlmIVf094u30Cj4gcSf_WKL33lHh8KgF0BNAjSL9Q1rT87W1qA6yOg-pjG2QrARp1sCD6myuS9O-oNtCvR3fw6OZoeecBRo1T2hknoKMlyVm0t0zUFMsgpzdzEQQU1RjGF8dThBhhrKEY70dDpy5lxD2eiZ8LmcSmHpG5Cz0_wQzzGDmyv9LlOriKeXAk6MCfqrGYrSAPGOdteihhHBFw-JeZnI5FDJY7-9mRqKWUifZSLWWRWC2tS6_XTTfX-xQWmq-m2Q"


# поиск в перечне нужной ца
response = requests.get(
    URL_audiences.format(HOST=HOST),
     headers={"Authorization":f"Bearer {token}"}
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
    "name": "тест редактирования",
    "body": "тест редактирования",
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

# успешное удаление шаблона
response = requests.delete(
    URL_templates_id.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешный перевод шаблона в статус удален
body = {
}

response = requests.put(
    URL_templates_disable.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())