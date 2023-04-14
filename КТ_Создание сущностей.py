import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates = "https://{HOST}/api/templates/email/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0NzYwODQsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0yMDc5NTUxNzYxIGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfZW1wcz9vcmdfb2lkPTIwNzk1NTI5NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW5mP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19jdHRzP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1Mjk0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbnZ0cz9vcmdfb2lkPTIwNzk1NTI5NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfcHJvZmlsZT9tb2RlPXcmb3JnX29pZD0yMDc5NTUyOTQzIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiI4YWVlMWFhZS0wNjc4LWM0NmItOGY0Zi00OGU4MzYxYTI1OGIiLCJ1cm46ZXNpYTpzYmpfaWQiOjIwNzk1NTE3NjEsImV4cCI6MTY4MTQ3OTY4NCwiaWF0IjoxNjgxNDc2MDg0LCJjbGllbnRfaWQiOiJQR1UifQ.Xm7YM_Ise5mXvXsv6cD-ZArpICB6SlIZeV52w1Qr_qyjQVZNvZ-66K_S1sYP6CfFINs3ZWLRpE-jDWOB8bg2ZSBy_Qj8WquDWwEh9IWbvh7Plpq3PrZrTsc3Otq4JX-Wee7uiyMleSD6dLmJ3aEhKVlDJqSDXG5p_oiR_3tKP6Qx_qJwMrlJmyqcC2Wrr5ybWqKhTXs7pXMzbnJqpSyupHvV4eIZf7ekjiWKLVAK4YMMVuj2q2q1i9Gi8qiNu4rmPkQlvF-PGjG2WYds-eGez9534O_-yn__ZWxaRTgqOdKtDl4dNb3SuNZAPF7qZAw38OeuU1l2AVTc7gMD2At0xQ"

# успешное создание ца
body = {
    "name": "КТ ГУ",
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
    "name": "КТ ГУ",
    "body": "КТ"
}

response = requests.post(
    URL_templates.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())