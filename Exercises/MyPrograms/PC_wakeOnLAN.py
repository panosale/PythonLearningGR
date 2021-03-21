# Απομακρυσμένη εκκίνηση (Wake on lan) ενός Η/Υ με χρήση της MAC address
# ΣΗΜΕΙΩΣΗ! Πρέπει να έχουν γίνουν οι απαραίτητες ρυθμίσεις στο BIOS και στα Windows του Η/Υ που θέλουμε να κάνουμε απομακρυσμένη εκκίνηση
from wakeonlan import send_magic_packet # Βιβλιοθήκη wakeonlan για αποστολή "μαγικού πακέτου" στην MAC address του Η/Υ
from pythonping import ping # Βιβλιοθήκη ping για έλεγχο αν άνοιξε ο Η/Υ
import time # Βιβλιοθήκη time για χρήση delay
send_magic_packet('XX.XX.XX.XX.XX.XX') # Δίνουμε την MAC address του Η/Υ που θέλουμε να γίνει απομακρυσμένη εκκίνηση
host = '192.168.1.XXX' # Η διεύθυνση IP του απομακρυσμένου Η/Υ (καλό είναι να είναι static)
hostname = 'SmallPC' # Το computer name του απομακρυσμένου Η/Υ (καλό είναι να είναι static)
result = (ping (host, count=1)).success() # 1 ping στην ΙΡ του απομακρυσμένου Η/Υ και επιστροφή της απάντησης .success() στην μεταβλητή result
while not result: # Επαναλήψη 1 ping μέχρι να απαντήσει σε ping ο απομακρυσμένος Η/Υ
    print (hostname, 'is offline.') # Εμφάνιση μηνύματος offline
    result = (ping (host, count=1)).success() # 1 ping στην ΙΡ του απομακρυσμένου Η/Υ και επιστροφή της απάντησης .success() στην μεταβλητή result
print ('*')
print ('*')
print ('*')
print (hostname, ' is ONLINE.') # Εμφάνιση μηνύματος online
time.sleep(10) # Αναμονή 10 sec πριν κλείσει το πρόγραμμα
