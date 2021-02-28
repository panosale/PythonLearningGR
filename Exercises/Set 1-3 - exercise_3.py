print ( '----- Set 1-3 - excercise_3 -----' )
# 3. Γράψτε ένα πρόγραμμα Python το οποίο διαβάζει ένα πραγματικό αριθμό x
# και υπολογίζει την τιμή συνάρτησης (δίνεται στο .pdf των ασκήσεων).
import math
def funcF ( x ):
    if x <= 0:
        return ( 3 * ( x ** 2 ) ) + 1
    elif x <= 3 and x > 0:
        return 2 * x + 1
    else:
        return math.sqrt ( 46 + x )
x = int ( input ( 'Give x: ') )
print ( 'f(' + str ( x ) + ') =', funcF ( x ) )
