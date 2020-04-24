print ( '----- Set 1-3 - excercise_7 -----' )
# 7. Γράψτε ένα πρόγραμμα Python το οποίο υπολογίζει τον μεγαλύτερο περιττό
# αριθμό μεταξύ των ακεραίων x, y και z.
x = int ( input ( 'Give x: ') )
y = int ( input ( 'Give y: ') )
z = int ( input ( 'Give z: ') )
x1 = ( x % 2 ) != 0
y1 = ( y % 2 ) != 0
z1 = ( z % 2 ) != 0
print ( x1 , ' - ' , y1 , ' - ' , z1)
