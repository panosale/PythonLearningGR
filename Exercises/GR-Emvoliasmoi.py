import requests
import datetime
url = 'https://data.gov.gr/api/v1/query/mdg_emvolio?date_from=2021-02-21&date_to=2021-02-28'
headers = {'Authorization':'Token afff74366084109b050512ce13d4b11c24bd3396'}
response = requests.get(url, headers=headers)
#with open('GR-Emvoliasmoi.txt', 'w', encoding='utf-8') as f:
#    json.dump(response.json(), f)
j = response.json()
j = sorted(j, key= lambda k: k['referencedate'], reverse=False) # Ascending sort by 'referencedate'
nomos = str(input("Δώστε νομό (Ελληνικά κεφαλαία π.χ. ΘΕΣΣΑΛΟΝΙΚΗΣ): "))
for p in j:
    if nomos == p['area']:
        date_time_obj = datetime.datetime.strptime(p['referencedate'], '%Y-%m-%dT%H:%M:%S')
        print('Area:', p['area'],
              ' - Date=', date_time_obj.date(),
              ' - DayTotal=', p['daytotal'],
              ' - Total=', p['totalvaccinations'])
