import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates = "https://{HOST}/api/templates/email/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEyMzM2MTgsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2VtcHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_bW9kZT13Jm9yZ19vaWQ9MjA3OTU1MTc5NSBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5MjgyIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiI0NjczODE5Yy0xMTc4LTFiZDctNjBjYS1hZDhiZjNkNWViYzYiLCJ1cm46ZXNpYTpzYmpfaWQiOjEwMDAyOTkyODIsImV4cCI6MTY4MTIzNzIxOCwiaWF0IjoxNjgxMjMzNjE4LCJjbGllbnRfaWQiOiJQR1UifQ.qk54JWBTWXV23hViYqJrKlkzmFIJ-rIGiGRkA-MbiHsqw8Q3vAfNA--DPj_qllFb5Gu3lbLrW7CuQGs_IO-8D3lf-KYy3tgcRRas4r-ZsndJhok-RCzddg-e1RZb55eUzQWHyE9t0Zady9ohKnpR3mYD2Q9sAzCaE1Kdj3X7x4wJR9N00dKmA7tNKFgbR9CgjkaQ-WLaM4lXc9NKYNd1j6ygYdlO4F-IJBvW6hVAyihYRkMv8IFXaKxhKgyHa3DzCUzsry33G65Z4oZpvvMHlUc9SYXNQzS58maiuij8F-rbPsRVfsjpuhIpl508gCketZURej-FOnj166flHyDB7A"

# успешное создание ца
body = {
    "name": "МСЭ ЧА",
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
    "name": "МСЭ ЧА",
    "body": "МСЭ"
}

response = requests.post(
    URL_templates.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())