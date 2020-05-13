print ( '----- Set 1-4 - excercise_2 -----' )
# 2. Γράψτε ένα πρόγραμμα το οποίο μετράει τον αριθμό των ψηφίων ενός φυσικού αριθμού.
print ( '\n***** Main exercise *****' )
n1 = int ( input ( 'Give an integer number: ') )
s = str ( n1 )
print ( 'The given number converted to string is:', s )
c = 0
for i in s:
    if i != '.':
        c += 1
print ( 'The digits of the given number are :', c )

### Παραλλαγή από panosale: Εμφανίζει ξεχωριστά τα ψηφία που βρίσκονται...
### ...αριστερά και δεξιά της υποδιαστολής και όλα μαζί συνολικά.
print ( '\n***** Alternative by panosale *****' )
n2 = float ( input ( 'Give a float number: ') )
cbefore = 0
cafter = 0
safter = ''
found = 0
s2 = str ( n2 )
for i in s2:
    if i != '.' and found == 0:
        cbefore += 1
    elif i != '.' and found == 1:
        cafter += 1
        safter = safter + i
    else:
        found = 1
if int ( safter ) == 0:
    cafter = 0
print ( 'The digits of the given number are :', cbefore, '.', cafter,
        ' and', cbefore + cafter, 'in total.' )
