import requests
from pprint import pprint

HOST = "armcrm-dev.test.gosuslugi.ru"
ID_audience = "2098"
audiences_updated_at = "2023-04-14T11:09:02.335775+03:00"
URL_audiences_update_status = "https://{HOST}/api/audiences/{ID_audience}/update-status/"

token = "eyJ2ZXIiOjEsInR5cCI6IkpXVCIsInNidCI6ImFjY2VzcyIsImFsZyI6IlJTMjU2In0.eyJuYmYiOjE2ODE0ODY5MDIsInNjb3BlIjoiaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19lbXBzP29yZ19vaWQ9MTAwMDMwMDY0OCZtb2RlPXcgaHR0cDpcL1wvZXNpYS5nb3N1c2x1Z2kucnVcL29yZ19pbmY_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3ZobHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX3Byb2ZpbGU_b3JnX29pZD0xMDAwMzAwNjQ4IGh0dHA6XC9cL2VzaWEuZ29zdXNsdWdpLnJ1XC9vcmdfaW52dHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvb3JnX2N0dHM_b3JnX29pZD0xMDAwMzAwNjQ4Jm1vZGU9dyBodHRwOlwvXC9lc2lhLmdvc3VzbHVnaS5ydVwvdXNyX2luZj9tb2RlPXcmb2lkPTEwMDAyOTkyODIiLCJpc3MiOiJodHRwOlwvXC9lc2lhLWRlbW8udGVzdC5nb3N1c2x1Z2kucnVcLyIsInVybjplc2lhOnNpZCI6IjFlYzFkNjM5LTllOTgtYjQ4NC04MmIxLTVmZGJkYTgzMTgxZiIsInVybjplc2lhOnNial9pZCI6MTAwMDI5OTI4MiwiZXhwIjoxNjgxNDkwNTAyLCJpYXQiOjE2ODE0ODY5MDIsImNsaWVudF9pZCI6IlBHVSJ9.lkRgdoVn0DfMJO37PgLFPckFsbv7Yq_AphJvsmWY7Lf-tTzI0PrpmO-fbq5HI4XtlNBgeuRyb50at_6bZ1LnBGV2gK5RxaeotkOCSXDbey0G0G_PQDiFAoc869LRPfdFMsBxAwFetA3x-X-tY2Q7olfcq-ye2aUpWR9N5pajyWYSVPc_ZNSNydk0_mW8fseIeFpsPLzmRnrQ2tkAtbhujE3ncPWQSOa-AEFYbKdXdyeVETs-OB28_0LP_1XwGPSG4PbdDSKI70nCg-nE2rhJHqs8m-3V-jVPWbHZjTt7XqaWe0UOmNk0BHIQyWiuodgZjnKsENZgrtaV2YFHopW_6g"

# перевод ца в статус черновик недоступно
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

print("")

# перевод ца в статус активна доступно
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