import requests

from datetime import date, timedelta, datetime

today = date.today()

start_day = today.day - 2

f = open(f'{today}.csv', 'w')
if today == date(2022, 7, 31):
    print(today + timedelta(days=21))
    f.write(f"Период действия программы истек. Свяжитесь с разработчиком \n\n")
    f.close()
    quit()

f.write(
    f"Developed by Yury Rozhkov \n\n  данные http://egr.gov.by за период: "
    f"{start_day}.{today.month}.{today.year}/{today.day}.{today.month}.{today.year} \n\n")

base_info_by_period = requests.get(
    f"http://egr.gov.by/api/v2/egr/getAddressByPeriod/23.11.2021/26.11.2021").json()
for sub in base_info_by_period:
    # print(sub)
    adress = sub['nsi00202']['vnsfull']
    if adress[0:9] != 'Брестская':
        continue
    ngrn = sub['ngrn']
    dfrom = sub['dfrom'][0:10]
    # tel_num = sub['vtels']
    if 'vtels' in sub:
        tel_num = sub['vtels']
    else:
        tel_num = '№ телефона не обнаружен'

    biz_type = requests.get((f"http://egr.gov.by/api/v2/egr/getVEDByRegNum/{ngrn}")).json()[0]['nsi00114']['vnvdnp']




    if requests.get((f"http://egr.gov.by/api/v2/egr/getIPFIOByRegNum/{ngrn}")).status_code == 200:
        name_ip = requests.get((f"http://egr.gov.by/api/v2/egr/getIPFIOByRegNum/{ngrn}"))
        f.write(f"{'k'}; {ngrn}; {dfrom}; {adress}; {tel_num}; {biz_type}\n")
    elif requests.get((f"http://egr.gov.by/api/v2/egr/getJurNamesByRegNum/{ngrn}")).status_code == 200:
        name_jur = requests.get((f"http://egr.gov.by/api/v2/egr/getJurNamesByRegNum/{ngrn}"))
        f.write(f"{name_jur.json()[0]['vnaim']}; {ngrn}; {dfrom}; {adress}; {tel_num}; {biz_type}\n")
    else:
        f.write(f"не определено; {ngrn}; {dfrom}; {adress}; {tel_num}; {biz_type}\n")

    # try:
    #     print(f"{name_ip.json()[0]['vfio']}; {ngrn}; {dfrom}; {adress}; {tel_num}; {biz_type}\n")
    # except:
    #     print(f"{name_jur.json()[0]['vnaim']}; {ngrn}; {dfrom}; {adress}; {tel_num}; {biz_type}\n")

f.close()
