import requests

from datetime import date

today = date.today()

start_day = today.day - 7

# f = open('subs.csv', 'w')
# base_info_by_period = requests.get((f"http://egr.gov.by/api/v2/egr/getBaseInfoByPeriod/{start_day}.{today.month}.{today.year}/{today.day}.{today.month}.{today.year}")).json()
# f.write(f"Developed by Yury Rozhkov \n\n  данные http://egr.gov.by за период: {start_day}.{today.month}.{today.year}/{today.day}.{today.month}.{today.year} \n\n")
# for sub in base_info_by_period:
#     if sub['nsi00212CRT']['vnuzp'] == 'Администрация Московского района г Бреста' or sub['nsi00212CRT'][
#         'vnuzp'] == 'Администрация Ленинского района г Бреста':
#         name_jur = requests.get((f"http://egr.gov.by/api/v2/egr/getJurNamesByRegNum/{sub['ngrn']}"))
#         name_ip = requests.get((f"http://egr.gov.by/api/v2/egr/getIPFIOByRegNum/{sub['ngrn']}"))
#         try:
#             f.write(f"{name_ip.json()[0]['vfio']}, {sub['ngrn']}, {sub['dfrom']}, {sub['nsi00212']['vnuzp']}\n")
#         except:
#             f.write(f"{name_jur.json()[0]['vnaim']}, {sub['ngrn']}, {sub['dfrom']}, {sub['nsi00212']['vnuzp']}\n")
base_info_by_period = requests.get('http://www.portal.nalog.gov.by/grp/getData?unp=291724708')
print(base_info_by_period.text)

# f.close()
