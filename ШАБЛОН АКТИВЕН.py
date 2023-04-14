import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"

ID_template = "381"
URL_templates_disable = "https://{HOST}/api/templates/email/{ID_template}/disable/"
URL_templates_deactivate = "https://{HOST}/api/templates/email/{ID_template}/deactivate/"
URL_templates_activate = "https://{HOST}/api/templates/email/{ID_template}/activate/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0NjE2ODksInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19lbXBzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3ZobHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_b3JnX29pZD0xMDAwMzAwNjQ4IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW52dHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvdXNyX2luZj9tb2RlPXcmb2lkPTEwMDAyOTkyODIiLCJpc3MiOiJodHRwOlwvXC9lc2lhLWRlbW8udGVzdC5nb3N1c2x1Z2kucnVcLyIsInVybjplc2lhOnNpZCI6IjRjMDgyZjkzLTJmM2QtZmVkNi0yOTdiLTU1ZmEwYjA0Y2RkZSIsInVybjplc2lhOnNial9pZCI6MTAwMDI5OTI4MiwiZXhwIjoxNjgxNDY1Mjg5LCJpYXQiOjE2ODE0NjE2ODksImNsaWVudF9pZCI6IlBHVSJ9.p3Rttv094Z6E4uztz2b7GdGypYBA33TDTL4npKRMU-S5nxwAwplndkjhMctyCcZ5rr7p-rJoB2ituMbyBH0XEjTOZ5wYXpy1LuXVlNco24fA-sX5soaZhC1MOwDeRA9eJy6mcmPeFUUN6tce6MLhOTUuRhr4-AyjwHhqkPnG471SnhLTCVVXb24f39_BuJ2Z0cdTIxzp-fIM7tKzztuHLU3IC9m8vh07-0GutSBOmjaxsf595dBao-0kwrCCYqJK8zooec3Sph2W-rtOaK5Ibc0lTlHDB2cMVhVr5WKVXfvs9cvBUhIBi-aFAAk3oEdJYNcsvzGLaJwuoRIEH_6pPQ"


# перевод шаблона в статус активен недоступно
body = {
}

response = requests.put(
    URL_templates_activate.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response.json())

print("")

# перевод шаблона в статус черновик доступно
body = {
}

response = requests.put(
    URL_templates_deactivate.format(HOST=HOST, ID_template=ID_template),
    headers={"Authorization": f"Bearer {token}"},
    data=body,
)
pprint(response)




