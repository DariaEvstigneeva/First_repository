import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates = "https://{HOST}/api/templates/email/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0ODAxNzUsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19wcm9maWxlP29yZ19vaWQ9MTAwMDI5ODkyMiBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MTAwMDI5ODkyMiZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5NjgxIGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfdmhscz9vcmdfb2lkPTEwMDAyOTg5MjImbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfZW1wcz9vcmdfb2lkPTEwMDAyOTg5MjImbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MTAwMDI5ODkyMiZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19jdHRzP29yZ19vaWQ9MTAwMDI5ODkyMiZtb2RlPXciLCJpc3MiOiJodHRwOlwvXC9lc2lhLWRlbW8udGVzdC5nb3N1c2x1Z2kucnVcLyIsInVybjplc2lhOnNpZCI6IjAzNDA1YTZmLWQxYWQtNWU2OS1jNWQ0LTg4M2IwOGEwYzAwNiIsInVybjplc2lhOnNial9pZCI6MTAwMDI5OTY4MSwiZXhwIjoxNjgxNDgzNzc1LCJpYXQiOjE2ODE0ODAxNzUsImNsaWVudF9pZCI6IlBHVSJ9.UGmy7urk7VC9ZdKv8EVc4zjfTxV6LsDRn37FquBbegeHqoNMa-jm8ZuvNaLEqHE1coVSTAbHOrGQ0q8o4L0szCh80ReMKMthqQ4JQCV4PxKMgy-l23ttITIDvJoVRPbUI1TSW-rOSW8cqKeRFP5GObjrRjDVJNlM4QDw1xjkcHIZLLeInP2_uC2ixA5B0SG-qrc3vX-SR4KiFLoPGqU-2GNSqUXgOsPhSUe8_dgX6WL85kQDNFMQ8RRfHcLZsZvRch5TNujXuG4IOz16A6opXg3YYqRuiasu5MeMZsEO0odeJZzeNOV7lcbNNs8jnZAGnsoEHRn7FBWj-3hYaFV-xQ"

# успешное создание ца
body = {
    "name": "ММЦ ЧА",
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
    "name": "ММЦ Ч_Ч",
    "body": "ММЦ"
}

response = requests.post(
    URL_templates.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())