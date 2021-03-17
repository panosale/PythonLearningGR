import requests
import datetime
#import json
url = 'https://data.gov.gr/api/v1/query/mdg_emvolio'#?date_from=2020-12-28&date_to=2021-02-28' # Σύνδεση στο URL με τα στοιχεία των εμβολιασμών. Από το ? μπορούμε να βάλουμε εύρος ημερομηνιών.
headers = {'Authorization':'Token afff74366084109b050512ce13d4b11c24bd3396'} # Χρήση έτοιμου token για σύνδεση. Μπορούμε να φτιάξουμε δικό μας για σύνδεση στο URL.
response = requests.get(url, headers=headers) # Αποθήκευση των δεδομένων του URL στην response.
#with open('GR-Emvoliasmoi.txt', 'w', encoding='utf-8') as f: # Άνοιγμα νέου αρχείου "GR-Emvoliasmoi.txt" για...
#    json.dump(response.json(), f) # ...αποθήκευση των στοιχείων της response (πρέπει να ενεργοποιηθεί και το import json στην γραμμή 3).
response = sorted(response.json(), key = lambda k: k['referencedate'], reverse = False) # Αύξουσα ταξινόμηση του responce βάσει του πεδίου "referencedate"
nomos = str(input("Δώστε νομό (Ελληνικά κεφαλαία π.χ. ΘΕΣΣΑΛΟΝΙΚΗΣ): ")) # Εισαγωγή από τον χρήστη του νομού ελέγχου.
date_from = datetime.datetime.strptime(str(input("Από... (ΕΕΕΕ-ΜΜ-ΗΗ): ")),'%Y-%m-%d') # Εισαγωγή από τον χρήστη της ημερομηνίας ελέγχου Από....
date_to = datetime.datetime.strptime(str(input("έως... (ΕΕΕΕ-ΜΜ-ΗΗ): ")),'%Y-%m-%d') # Εισαγωγή από τον χρήστη της ημερομηνίας ελέγχου Έως....
for f in response:
    date_time_obj = datetime.datetime.strptime(f['referencedate'], '%Y-%m-%dT%H:%M:%S') # Μετατροπή του πεδίου "referencedate" σε μεταβλητή τύπου datetime
    if nomos == f['area'] and (date_time_obj.date() >= date_from.date() and date_time_obj.date() <= date_to.date()): # Αν ο νομός και οι ημερομηνίες ταιριάζουν με αυτά που έδωσε ο χρήστης τότε...
        print('Area:', f['area'], # ...εκτύπωση νομού...
              ' - Date=', date_time_obj.date(), # ...εκτύπωση ημεομηνίας εβολιασμού...
              ' - DayTotal=', f['daytotal'], # ...εκτύπωση συνολικών εμβολιασμών ημέρας...
              ' - Total=', f['totalvaccinations']) # ...εκτύπωση συνολικών εμβολιασμών νομού μέχρι την ημερομηνία.