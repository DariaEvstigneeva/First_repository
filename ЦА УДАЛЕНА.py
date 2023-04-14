import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
ID_audience = "2142"
audiences_updated_at = "2023-04-14T11:17:15.386857+03:00"
URL_audiences_update_status = "https://{HOST}/api/audiences/{ID_audience}/update-status/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0NTk1NzAsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2VtcHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_bW9kZT13Jm9yZ19vaWQ9MjA3OTU1MTc5NSBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0yMDc5NTUxNzk1Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ192aGxzP29yZ19vaWQ9MjA3OTU1MTc5NSZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5MjgyIiwiaXNzIjoiaHR0cDpcL1wvZXNpYS1kZW1vLnRlc3QuZ29zdXNsdWdpLnJ1XC8iLCJ1cm46ZXNpYTpzaWQiOiJjM2YxNGIzNy1jMDA0LWE1NmMtNGFjNS01ZWI4MGI1YmNhNzAiLCJ1cm46ZXNpYTpzYmpfaWQiOjEwMDAyOTkyODIsImV4cCI6MTY4MTQ2MzE3MCwiaWF0IjoxNjgxNDU5NTcwLCJjbGllbnRfaWQiOiJQR1UifQ.HvPKp3oVoDs65bTlFELyHGzULXTitHGk_VC3vUyySL7hT6OtZi-aVAzd7BlOZsuablkATlmNS1pQdzlmV3g5aqI9HcTm1_tRo960FN4nITZfVdAhFv3l9dTobX9o1SSWsSmt01_adISKqOrWPsmb-iF2shS3Zg-G4_Mx9fMz_O4rZOjxxvZdJ4sjRu2j8d-hqCCe_QwTeFzmso2XxhjiMI_bkZ3JiLM_lSZtGXumJAxfIK9Chk6TmJmFBpN_fF0cKSfbpMy8L_onAVXfc9dwdta9cv0UowbwTyGae27_TTe75YxDgZ1bjkujm5WvkMgQs-yHQkZp5GY70aDRtGondg"

# перевод ца в статус черновик ненедоступно
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

# перевод ца в статус активна недоступно
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

# перевод ца в статус удалена недоступно
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