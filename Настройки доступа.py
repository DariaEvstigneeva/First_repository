import requests
from pprint import pprint
from array import array

HOST = "armcrm-dev.test.gosuslugi.ru"

URL_templates_access = "https://{HOST}/api/templates/377/access/"
URL_templates_available_orgs = "https://{HOST}/api/templates/377/access/available-orgs/"

URL_audiences_access = "https://{HOST}/api/audiences/377/access/"
URL_audiences_available_orgs = "https://{HOST}/api/audiences/377/access/available-orgs/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEzMDY3OTEsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2VtcHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_bW9kZT13Jm9yZ19vaWQ9MjA3OTU1MTc5NSBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5MjgyIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiIyYzdmZDdlYi00NzI0LTg4YjItODc4Zi0yNDA5YjUwM2FmYjQiLCJ1cm46ZXNpYTpzYmpfaWQiOjEwMDAyOTkyODIsImV4cCI6MTY4MTMxMDM5MSwiaWF0IjoxNjgxMzA2NzkxLCJjbGllbnRfaWQiOiJQR1UifQ.TKfp9F9op8RYtSptZyE_rY8cqlTAZlA7OehrJGQTBWDBwINnYvRZ8YWufxwz5FJbYHEwE8K5hzrqllzAWa8yiy5FKCkA9HTUEekdOBzW69lODnUVjMz4w67nSx-vjtiQJyhOiclvGjpASkYt2V965tvxlqJM4N1s0xQn1_O_Sl74pkyXJk3W00SazTxPXsb7nW0r5hoo66xjSZPoFlkuc-7YFkl0aTrP0E4zKXURf1PkdMiJMp4sgT4gUq0ocAaEg3g7l7zBO2y9mOCF_8EGXR8qdsFFegNetYaXdLwRD0SKWU4OrkPGN0L1qbfg8KpATBSd0vp1FYr2cyEvvDJvVw"

# успешный просмотр текущих настроек доступа ца
response = requests.get(
    URL_audiences_access.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешный просмотр списка организаций для настроек доступа ца
response = requests.get(
    URL_audiences_available_orgs.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешное редактирование настроек доступа ца
body = {
    "privileged_orgs": ['1', '2'],
    "is_every_org_privileged": False,
    "is_public": False,
}

response = requests.put(
    URL_audiences_access.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")
print("")

# успешный просмотр текущих настроек доступа шаблона
response = requests.get(
    URL_templates_access.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешный просмотр списка организаций для настроек доступа шаблона
response = requests.get(
    URL_templates_available_orgs.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
)
pprint(response.json())

print("")

# успешное редактирование настроек доступа шаблона
body = {
    "privileged_orgs": ['1', '2'],
    "is_every_org_privileged": False,
    "is_public": False,
}

response = requests.put(
    URL_templates_access.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())