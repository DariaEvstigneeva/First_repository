import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates = "https://{HOST}/api/templates/email/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEyMjQ4NTQsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2VtcHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_bW9kZT13Jm9yZ19vaWQ9MjA3OTU1MTc5NSBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5MjgyIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiI2Y2U1NTQ3NC1mZmM5LTYzYTYtNWE2Yi1kNGJmY2IzYzBlZTUiLCJ1cm46ZXNpYTpzYmpfaWQiOjEwMDAyOTkyODIsImV4cCI6MTY4MTIyODQ1NCwiaWF0IjoxNjgxMjI0ODU0LCJjbGllbnRfaWQiOiJQR1UifQ.peKChf4TFN55__je_4fdoyz0XuUeA3nKvc_0Zo3Uor4LsFhFgG7OqST_rv1rqBFoSHvxBwORwYolYadbp7CjynnjXnMS2py_jpw3J9OokaJIUZIseBoeIagkhYwRds7F2yxdFUTrMVpY2Kpa1bYCT7uCnS0XAmwP2LIKE0keXY22qK7c2BFKkPNj13CmPqdQi1lp4s1Y41iHTOUQUuw8Ub8eI65ZmKxgRH2jgW4TheXHhNxK9Kjgsgi90vH61igf867RoIMv5LWyuTsZYDJvleEVF29z8BKNXbIm6wI5XaU7FsFS2RSlSn9jIbyMF8xFFsGf1Hfm0ZMGtlZrnYA9tA"

# успешное создание ца
body = {
    "name": "МСЭ ЧА4",
    "category": "PHYSICAL"
}

response = requests.post(
    URL_audiences.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())

print("")

# создание шаблона недоступно
body = {
    "name": "МСЭ ЧА2"
}

response = requests.post(
    URL_templates.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())