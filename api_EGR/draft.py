import requests

from datetime import date, timedelta, datetime

name_ip = requests.get((f"http://egr.gov.by/api/v2/egr/getIPFIOByRegNum/491654024")).status_code == 200:

print(name_ip)