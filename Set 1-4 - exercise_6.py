print ( '----- Set 1-4 - excercise_6 -----' )
# 6. Γράψτε ένα πρόγραμμα το οποίο ελέγχει αν μια λέξη είναι παλινδρομική,
# δηλαδή διαβάζεται το ίδιοκαι από δεξιά και από αριστερά.
# Η λέξη πρέπει να δίνεται από τον χρήστη.
s = input('Give a string: ')
def CutSpaces(s):
    new_s = ''
    for i in range(0, len(s)):
        if s[i] != ' ':
            new_s = new_s + s[i]
    return new_s
def ReverseString(s):
    new_s = ''
    for i in range(len(s), 0, -1):
        new_s = new_s + s[i-1]
    return new_s
if CutSpaces(s) == ReverseString(CutSpaces(s)):
    print (s, 'is reversable')
else:
    print (s, 'is NOT reversable')

    
