print ( '----- Set 1-4 - excercise_1 -----' )
# 1. Γράψτε ένα πρόγραμμα που βρίσκει και τυπώνει τον αριθμό των φωνηέντων σε μια ακολουθία
# χαρακτήρων. Τα φωνήεντα είναι, φυσικά, οι χαρακτήρες a, e, i, o, u.
fonienta = ['a', 'e', 'i', 'o', 'u']
s = str ( input ( 'Give a string: ') )
n = 0
for c in s:
    if c in fonienta: n += 1
print ( 'The vowels in given string are :' , n )

