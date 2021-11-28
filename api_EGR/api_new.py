from datetime import date, datetime, timedelta

import requests

sub_dict = {}
today = datetime.today()
f_name = (datetime.today()).strftime("%d_%m_%Y %H_%M_%S")

delta = timedelta(days=2)  # период запроса: today - УКАЗАТЬ количесвто дней

start_day = (today - delta).strftime("%d.%m.%Y")

f = open(f'{f_name}.csv', 'w')
if today == date(2022, 7, 31):
    f.write(f"Период действия программы истек. Свяжитесь с разработчиком \n\n")
    f.close()
    quit()
today = today.strftime("%d.%m.%Y")

f.write(
    f"Developed by Yury Rozhkov \n\n  данные http://egr.gov.by за период: {start_day} - {today} \n\n")

base_info_by_period = requests.get(f"http://egr.gov.by/api/v2/egr/getBaseInfoByPeriod/{start_day}/{today}").json()

for sub in base_info_by_period:
    ngrn = sub['ngrn']
    event = sub['nsi00208']['vnscrtp']
    typ_of_sub = sub['nsi00211']['vnvobp']
    dfrom = sub['dfrom'][0:10]
    adress_request = requests.get(f"http://egr.gov.by/api/v2/egr/getAddressByRegNum//{ngrn}")
    if adress_request.status_code == 204:
        adress = 'адрес проверьте вручную'
        tel_num = '№ телефона не обнаружен'
    elif adress_request.status_code == 200:
        adres_conteiner = adress_request.json()[0]
        adress = adress_request.json()[0]['nsi00202']['vnsfull']
        if 'vtels' in adres_conteiner:

            tel_num = adres_conteiner['vtels']
        else:
            tel_num = '№ телефона не обнаружен'
    else:
        adress = str(adress_request.status_code)
        tel_num = str(adress_request.status_code)

    biz_type = requests.get((f"http://egr.gov.by/api/v2/egr/getVEDByRegNum/{ngrn}")).json()[0]['nsi00114']['vnvdnp']
    if requests.get((f"http://egr.gov.by/api/v2/egr/getIPFIOByRegNum/{ngrn}")).status_code == 200:
        name_ip = requests.get((f"http://egr.gov.by/api/v2/egr/getIPFIOByRegNum/{ngrn}")).json()[0]['vfio']
        sub_dict[ngrn] = (f"{ngrn} ; {name_ip} ; {dfrom} ; {adress} ; {tel_num} ; {biz_type}")
    elif requests.get((f"http://egr.gov.by/api/v2/egr/getJurNamesByRegNum/{ngrn}")).status_code == 200:
        name_jur = requests.get((f"http://egr.gov.by/api/v2/egr/getJurNamesByRegNum/{ngrn}")).json()[0]['vnaim']
        sub_dict[ngrn] = (f"{ngrn} ; {name_jur} ; {dfrom} ; {adress} ; {tel_num} ; {biz_type}")
    else:
        sub_dict[ngrn] = (f"{ngrn} ; не определено ; {dfrom} ; {adress} ; {tel_num} ; {biz_type}")

sorted(sub_dict.keys())
for key in sorted(sub_dict.keys()):
   f.write(f'{sub_dict[key]}\n')


f.close()
