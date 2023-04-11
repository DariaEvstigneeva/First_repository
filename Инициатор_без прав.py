import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences_id = "https://{HOST}/api/audiences/2131/"
URL_audiences_copy = "https://{HOST}/api/audiences/2131/clone/"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates_id = "https://{HOST}/api/templates/email/376/"
URL_templates_copy = "https://{HOST}/api/templates/email/376/clone/"
URL_templates = "https://{HOST}/api/templates/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEyMjY2MDIsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19lbXBzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0yMDc5NTUyOTY0IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19wcm9maWxlP21vZGU9dyZvcmdfb2lkPTEwMDAzMDA2NDggaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbnZ0cz9vcmdfb2lkPTEwMDAzMDA2NDgmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfY3R0cz9vcmdfb2lkPTEwMDAzMDA2NDgmbW9kZT13IiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiJiNTM3ZjA5Mi1hM2YyLTZkNzktOWZmZi0zOGJkNTYzNmQ0NzQiLCJ1cm46ZXNpYTpzYmpfaWQiOjIwNzk1NTI5NjQsImV4cCI6MTY4MTIzMDIwMiwiaWF0IjoxNjgxMjI2NjAyLCJjbGllbnRfaWQiOiJQR1UifQ.XhbuTxZsY6nL1F-oAQy7FriX2h8elvz6in1loNGdpjZhmK8Q884uHDVRi2TUXz6VA1m8AzTdjBZRww7EVJPuq_McOyf--4VLMNtpyLsWKngWHMwEhq2EH9nILmD3mpnimIuHifJWQNXyySsACOyBnWnyTPhPJvIUkjkWQ_UEy_9fcOqXCN_Y3ZzkxYivW0Pfv6XTnxZGZ7Rb4SJjf5eLV-h1wyrI3e41KoACa8hrlRwX9NvwlxiowpMoanFJitWZN8zi7xCyfMdqHI2iPuqMsMTXETzbI93_MzsqHaeUa-CL5FzWtsykPyOZ0ipiAuI4s6YD5nxkzEL5Pxtw8MNrmQ"

# получение ца (Страница не найдена)
response = requests.get(
    URL_audiences_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# копирование ца (Страница не найдена)
body = {
}

response = requests.post(
    URL_audiences_copy.format(HOST=HOST),
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

# редактирование недоступно (Страница не найдена)
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

# получение шаблона (Страница не найдена)
response = requests.get(
    URL_templates_id.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# копирование шаблона (Страница не найдена)
body = {
}

response = requests.post(
    URL_templates_copy.format(HOST=HOST),
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

# редактирование недоступно (Страница не найдена)
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