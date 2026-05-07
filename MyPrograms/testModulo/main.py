def is_sorted(lst):
    lst = sorted(lst)
    for i in range(len(lst) -1):
        if lst[i+1] - lst[i] != 1:
            return False
    return True

modulo = int(input("Δώσε το modulo: "))
prim_root = int(input("Δώσε την υποψήφια Πρωτογενή Ρίζα: "))
mod_arr = []
mod_arr.clear()
for i in range(1, modulo):
#    pwr = pow(prim_root, i)
#    mod = pwr % modulo
    mod_arr.append(pow(prim_root, i) % modulo)
if is_sorted(mod_arr):
    print('Το ', prim_root, ' ΕΙΝΑΙ Πρωτογενής Ρίζα του ', modulo, '.', sep="")
else:
    print('Το ', prim_root, ' ΔΕΝ ΕΙΝΑΙ Πρωτογενής Ρίζα του ', modulo, '.', sep="")

print(sorted(mod_arr))
