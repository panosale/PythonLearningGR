print ( '----- Set 1-4 - excercise_3 -----' )
# 3. Γράψτε ένα πρόγραμμα το οποίο τυπώνει τον πίνακα της προπαίδειας στην εξής μορφή
# 1  2   3  ...9
# 2  4   6  ...18
# ...
# 9  18  27 ...81

n_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range (1, len (n_lst) + 1 ):
    print (n_lst)
    n_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range (0, len (n_lst) ):
        n_lst[j] = n_lst[j] * (i + 1)

# Ή η παρακάτω παραλλαγή με τη χρήση σταθερών.

print ( '----- Set 1-4 - excercise_3 -----' )
# 3. Γράψτε ένα πρόγραμμα το οποίο τυπώνει τον πίνακα της προπαίδειας στην εξής μορφή
# 1  2   3  ...9
# 2  4   6  ...18
# ...
# 9  18  27 ...81

const_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n_lst = const_lst.copy()
for i in range (1, len (n_lst) + 1 ):
    print (n_lst)
    n_lst = const_lst.copy()
    for j in range (0, len (n_lst) ):
        n_lst[j] = n_lst[j] * (i + 1)
