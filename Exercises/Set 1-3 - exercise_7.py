print ( '----- Set 1-3 - excercise_7 -----' )
# 7. Γράψτε ένα πρόγραμμα Python το οποίο υπολογίζει τον μεγαλύτερο περιττό
# αριθμό μεταξύ των ακεραίων x, y και z.
x = int ( input ( 'Give x: ') )
y = int ( input ( 'Give y: ') )
z = int ( input ( 'Give z: ') )
# Απλός έλεγχος των μονών/ζυγών αριθμών που δόθηκαν.
x1 = ( x % 2 ) != 0
y1 = ( y % 2 ) != 0
z1 = ( z % 2 ) != 0
m = 0
if ( x % 2 != 0 ) :
    m = x
if ( y % 2 != 0 ) and ( y > m ):
    m = y
if ( z % 2 != 0 ) and ( z > m ):
    m = z
print ( x1 , ' - ' , y1 , ' - ' , z1 ,
        '\nMaximum of given odd nambers is' , m)
