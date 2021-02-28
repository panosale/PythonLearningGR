import requests
import datetime
#import json
url = 'https://data.gov.gr/api/v1/query/mdg_emvolio?date_from=2020-12-28&date_to=2021-02-28'
headers = {'Authorization':'Token afff74366084109b050512ce13d4b11c24bd3396'}
response = requests.get(url, headers=headers)
#with open('GR-Emvoliasmoi.txt', 'w', encoding='utf-8') as f:
#    json.dump(response.json(), f)
j = response.json()
j = sorted(j, key= lambda k: k['referencedate'], reverse=False) # Ascending sort by 'referencedate'
nomos = str(input("Δώστε νομό (Ελληνικά κεφαλαία π.χ. ΘΕΣΣΑΛΟΝΙΚΗΣ): "))
date_from = str(input("Από... (ΕΕΕΕ-ΜΜ-ΗΗ): "))
date_to = str(input("έως... (ΕΕΕΕ-ΜΜ-ΗΗ): "))
d_from = datetime.datetime.strptime(date_from,'%Y-%m-%d')
d_to = datetime.datetime.strptime(date_to,'%Y-%m-%d')
for p in j:
    date_time_obj = datetime.datetime.strptime(p['referencedate'], '%Y-%m-%dT%H:%M:%S')
    if nomos == p['area'] and (date_time_obj.date > d_from or date_time_obj.date < d_to): #Θέλει διόρθωση
        print('Area:', p['area'],
              ' - Date=', date_time_obj.date(),
              ' - DayTotal=', p['daytotal'],
              ' - Total=', p['totalvaccinations'])
