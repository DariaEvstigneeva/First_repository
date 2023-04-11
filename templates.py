import requests
import sys
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
API_URL = "https://{HOST}/api/{module}/?status=DRAFT"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEyMDkxOTksInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2VtcHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_bW9kZT13Jm9yZ19vaWQ9MjA3OTU1MTc5NSBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5MjgyIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiI4YjIwZTkzNy0yOGNiLTVhY2MtNTI0Yy01MTg5MWViNzNkNGIiLCJ1cm46ZXNpYTpzYmpfaWQiOjEwMDAyOTkyODIsImV4cCI6MTY4MTIxMjc5OSwiaWF0IjoxNjgxMjA5MTk5LCJjbGllbnRfaWQiOiJQR1UifQ.pd-OTbGNxdUuG-VF0ezgIDOwYFe1B1IpF2nWF0evDAXcYhK9dXrQ_oft-Fq4qPekU-IoUTUgVECm2VjQjopBTt737kYwmRgQEIUBIUU9fdah1H3Rd9mYhjBFPYjmvcQRa2YXYeLSJWIo1VLm0rccqcxwLoPKKT9V7eVNxPoC67vf9s1jkErxTcHGbdcnLXU2Tj1nenbMymxOGF5nfr065Mo7gMSKS2YgijrPuQPd8iDnF8j-GKcZTh6U584YjYtCaAfalkBwO8ULWRAblroYy2qMyx2XoyRvYMqWdW6FCif98yp7n10saY_ikmSHS5y43zdU4mryJsErTgF8wqrCJw"


try:
    http_method = sys.argv[1]
    module = sys.argv[2]
except IndexError:
    print("Необходимо передать два параметра:\n\t1 - http метод (get, post, etc.)\n\t2 - модуль (audiences, templates etc.)")
    print("\tПример: python templates.py get audiences")
    exit(1)


try:
    requests_method = getattr(requests, http_method.lower().strip())
except AttributeError:
    print(f"Не существует http метода {http_method}")
    exit(1)

response = requests_method(
    API_URL.format(HOST=HOST, module=module.strip().lower()),
     headers={"Authorization":f"Bearer {token}"},
)
pprint(response.json())