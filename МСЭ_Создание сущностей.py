import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates = "https://{HOST}/api/templates/email/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0ODAwMzUsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2VtcHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_bW9kZT13Jm9yZ19vaWQ9MjA3OTU1MTc5NSBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5MjgyIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiIxYmQ3ZmU2MC1kZWE5LTZkYzYtNDJjYy00NzNmYjhmNDg0MzQiLCJ1cm46ZXNpYTpzYmpfaWQiOjEwMDAyOTkyODIsImV4cCI6MTY4MTQ4MzYzNSwiaWF0IjoxNjgxNDgwMDM1LCJjbGllbnRfaWQiOiJQR1UifQ.pMJTwTTH7d1mqCIXZeywZSDPmKpScgO7JtMhoUuaaVZFndCzDC_YBW5re2vc0iBMLAEW__mhIax-wi-GlHB8N1N8wcDeW1JtoG9kBkIynJwmijc9TwpHR6H5Zjo2pyNm5NVQVsGiw3K11w6jrrgAdFPLzBMxJBhGVX4lJFHmC9dHgDYBw19pFkqCIVZTN6zVnz0E-MlTHSYJKI2oXE2ypsSScEcOHWFKluuEwueqUZ-xtNzfovVBh-KXpwBfCHS7zNsG5OJGXbzVGzd1fOA3iwYqoToQjOSeMHO0eDLOOfqeQLehfrJuWyGIRLB2EMyY3tqdUmC839qqQZ6bcA4aFQ"

# успешное создание ца
body = {
    "name": "МСЭ ГУ",
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
    "name": "МСЭ 1",
    "body": "МСЭ"
}

response = requests.post(
    URL_templates.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())