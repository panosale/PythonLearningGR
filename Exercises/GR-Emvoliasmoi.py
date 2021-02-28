import requests
import datetime
import json
url = 'https://data.gov.gr/api/v1/query/mdg_emvolio?date_from=2021-02-21&date_to=2021-02-28'
headers = {'Authorization':'Token afff74366084109b050512ce13d4b11c24bd3396'}
response = requests.get(url, headers=headers)
with open('GR-Emvoliasmoi.txt', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f)
nomos = str(input("Δώστε νομό (Ελληνικά κεφαλαία π.χ. ΘΕΣΣΑΛΟΝΙΚΗΣ): "))
j = response.json()
for p in j:
    if nomos == p['area']:
        date_time_obj = datetime.datetime.strptime(p['referencedate'], '%Y-%m-%dT%H:%M:%S')
        print(p['area'], ' - ', p['areaid'],
              ' - Date=', date_time_obj.date(),
              ' - DayTotal=', p['daytotal'],
              ' - Total=', p['totalvaccinations'])
        
