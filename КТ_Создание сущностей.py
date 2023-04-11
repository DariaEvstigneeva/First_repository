import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates = "https://{HOST}/api/templates/email/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODEyMjc1MzAsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19lbXBzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3ZobHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_b3JnX29pZD0xMDAwMzAwNjQ4IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW52dHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvdXNyX2luZj9tb2RlPXcmb2lkPTEwMDAyOTkyODIiLCJpc3MiOiJodHRwOlwvXC9lc2lhLWRlbW8udGVzdC5nb3N1c2x1Z2kucnVcLyIsInVybjplc2lhOnNpZCI6IjZmYjBjYWYzLTBkYzktYTY2MS04YWQ1LTIwM2U4NWUwNzA4MiIsInVybjplc2lhOnNial9pZCI6MTAwMDI5OTI4MiwiZXhwIjoxNjgxMjMxMTMwLCJpYXQiOjE2ODEyMjc1MzAsImNsaWVudF9pZCI6IlBHVSJ9.Lx2_5vRV25HO7RnlOybx-nddFdnZbx8FJQsEX9B0kEt-l7MRyxgoedWxlnb-n8BUTfCI0LpzYY88WJ-sdR6sXs2IkaIyxNyWjqSe4ufJ3ZVjllOnHzOeNw9iWpT7jxnD9VBSLMY2eTYq_9IgRLv9GSBxpVqdLBdj62vrRqPkr5DuqlOjJKe7-7sa3GwDFtmvhNFyhZHiGQVyHUn8EwAE1wgEQA5j-5qz4n3-QJSk4lIms-ReHXODIQZwbJrSzb3lavBgtnzZcTYl-j6Dk3EabyPsb7tbI9q_P8b6OtuVWhiOF0KoMRpViYDuvT_H0gJXcp72gcE_S6qAT47VL3-N6g"

# успешное создание ца
body = {
    "name": "КТ ЧА",
    "category": "PHYSICAL"
}

response = requests.post(
    URL_audiences.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())

print("")

# успешное создание шаблона
body = {
    "name": "КТ ЧА",
    "body": "КТ"
}

response = requests.post(
    URL_templates.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())