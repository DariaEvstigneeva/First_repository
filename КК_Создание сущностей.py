import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
URL_audiences = "https://{HOST}/api/audiences/"
URL_templates = "https://{HOST}/api/templates/email/"
token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0NzkxMzQsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0xMDAwMjk5NTQzJm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2ludnRzP29yZ19vaWQ9MTAwMDI5OTU0MyZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL3Vzcl9pbmY_bW9kZT13Jm9pZD0xMDAwMjk5Njg2IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfdmhscz9vcmdfb2lkPTEwMDAyOTk1NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfY3R0cz9vcmdfb2lkPTEwMDAyOTk1NDMmbW9kZT13IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfcHJvZmlsZT9vcmdfb2lkPTEwMDAyOTk1NDMgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19lbXBzP29yZ19vaWQ9MTAwMDI5OTU0MyZtb2RlPXciLCJpc3MiOiJodHRwOlwvXC9lc2lhLWRlbW8udGVzdC5nb3N1c2x1Z2kucnVcLyIsInVybjplc2lhOnNpZCI6IjQ2NTFlM2JlLTM0YjItZjcyYy05MzY0LWFhZDY2NDljMGI3YyIsInVybjplc2lhOnNial9pZCI6MTAwMDI5OTY4NiwiZXhwIjoxNjgxNDgyNzM0LCJpYXQiOjE2ODE0NzkxMzQsImNsaWVudF9pZCI6IlBHVSJ9.L5CmR3JFi9LGC6Ok6sAPYlYrn7hSnBv6nIHe2BF9MmA4omVA5X6aRit7zHHJREm8T3LXrZ5Z5kQyurTVHvPOiw4MO7JNVbQPqTFB1FpOtHCP3glGSFL_aWn8Ds1XbuBZZqF567G6uSt-3Q_TTDXwsM-LYdLkfBZzLNR17gHCE_y5VwXJ-mUQEIOUUkHINHIJBdPHnWTQqelFHCbGck66Gni-jVb-hyEv4ciL1BEcB2PPoBZ3SJOAwPvcWeFwqyrSailtaj4eAY5RiQZX3d9VG0XQ9GPFNak-rue9SlGvq41m77lt--4LI32-BA2E644YUnCX_wJelNVu0QDf7Mu8Kg"

# создание ца недоступно
body = {
    "name": "КК ЧА",
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
    "name": "КК ЧУ",
    "body": "КК"
}

response = requests.post(
    URL_templates.format(HOST=HOST),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)

pprint(response.json())