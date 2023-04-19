import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
ID_audience = "2167"
audiences_updated_at = "2023-04-14T19:15:03.287449+03:00"
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

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE3MzQwNTAsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0yMDc5NTUxNzYxIGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfZW1wcz9vcmdfb2lkPTIwNzk1NTI5NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19jdHRzP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbnZ0cz9vcmdfb2lkPTIwNzk1NTI5NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfcHJvZmlsZT9tb2RlPXcmb3JnX29pZD0yMDc5NTUyOTQzIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiJjY2Q1YjA5ZS05OTY0LTdiMWItM2QxYS04Mzk5MTc3YmJmMzMiLCJ1cm46ZXNpYTpzYmpfaWQiOjIwNzk1NTE3NjEsImV4cCI6MTY4MTczNzY1MCwiaWF0IjoxNjgxNzM0MDUwLCJjbGllbnRfaWQiOiJQR1UifQ.HeVPmO5s_haUWrEfIbfA8xd0wJpfuM6koeeeD7iERSa-u-c4vHRMsnrl1z_fsTBCqLfnmzmI4DYtztcDuzW0SQlbjvq5oShAyKLNSRrpRwsgTcRiLqgRWs0KB5hsS8m7PJZkIlH7_RMQyOj-NNGv9qVDRfo9agIo_B1uqEX11BEv3pG6BrgjH306p5MRyXRz9l8WqfU6M4yQM0VzpZQJJRL07WNOJXEjmmTfLqYuM1dhhljgVoUPkPLrx5dLNYLJZrP0mtz0SzYWjCoK8P_g7gfmdc-QCxuDz8qJWMgRr39jkZj2jxaWLmg_eVcqBq0JdZEXELAfEf8tmPId1c5deQ"

# поиск в перечне нужной ца
response = requests.get(
    URL_audiences.format(HOST=HOST),
     headers={"Authorization":f"Bearer {token}"},
     params={"search":ID_audience},
)
pprint(response.json())

print("")

# успешное получение ца
response = requests.get(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешное копирование ца
body = {
}

response = requests.post(
    URL_audiences_copy.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# редактирование ца недоступно
body = {
    "description": "тест редактирования",
    "name": "тест редактирования",
    "updated_at": audiences_updated_at
}

response = requests.put(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# перевод ца в статус черновик недоступен
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

# перевод ца в статус активна недоступен
body = {
    "status": "ACTIVE",
    "updated_at": audiences_updated_at
}

response = requests.patch(
    URL_audiences_update_status.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# перевод ца в статус удалена недоступен
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

# удаление ца недоступно
response = requests.delete(
    URL_audiences_id.format(HOST=HOST, ID_audience=ID_audience),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())