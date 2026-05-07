def is_sorted(lst):
    lst = sorted(lst)
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != 1:
            return False
    return True


modulo = int(input("Δώσε το modulo: "))
prim_root = int(input("Δώσε την υποψήφια Πρωτογενή Ρίζα: "))
mod_arr = []
mod_arr.clear()
for i in range(1, modulo):
    # pwr = pow(prim_root, i)
    # mod = pwr % modulo
    mod_arr.append(pow(prim_root, i) % modulo)
print("Για να είναι το " , prim_root , " Πρωτογενής Ρίζα του " , modulo , " πρέπει ο παρακάτω πίνακας να περιέχει όλους τους αριθμούς από το 1 έως το " , modulo - 1 , " (δηλ. modulo-1).", sep="")
print(sorted(mod_arr))
if is_sorted(mod_arr):
    print("Οπότε, το ", prim_root, " ΕΙΝΑΙ Πρωτογενής Ρίζα του ", modulo, ".", sep="")
else:
    print("Οπότε, το ", prim_root, " ΔΕΝ ΕΙΝΑΙ Πρωτογενής Ρίζα του ", modulo, ".", sep="")

