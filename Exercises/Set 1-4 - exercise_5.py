print ( '----- Set 1-4 - excercise_5 -----' )
# 5. Γράψτε ένα πρόγραμμα το οποίο ζητάει ένα θετικό ακέραιο n και υπολογίζει τον
# n-στό όρο της ακολουθίας Fibonacci.
# Υπενθυμίζουμε ότι οι όροι της ακολουθίας Fibonacci ορίζονται ως εξής:
# F0=0, F1=1 και Fn=Fn-1+Fn-2 για Fn>=2
n = int(input('Give n: '))
f, f1, f2 = 0, 0, 0
for i in range(0, n):
    if i < 2:
        f = i
    else:
        f  = f1 + f2
    f1 = f2
    f2 = f
    print(f)
