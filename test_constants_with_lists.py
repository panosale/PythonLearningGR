const_n = [1, 2, 3]
print ('*** Σωστή απόδοση σταθεράς σε μεταβλητή (1ος τρόπος)')
n = const_n.copy()
print ('n =', n, ' (Χρήση n = const_n.copy())')
n[0] = n[0] + 10
n[1] = n[1] + 10
n[2] = n[2] + 10
print ('n + 10 =', n)
print ('*** Σωστή απόδοση σταθεράς σε μεταβλητή (2ος τρόπος)')
n = const_n[:]
print ('n =', n, ' (Χρήση n = const_n[:])')
n[0] = n[0] + 10
n[1] = n[1] + 10
n[2] = n[2] + 10
print ('n + 10 =', n)
print()
print ('*** Λάθος απόδοση σταθεράς σε μεταβλητή.')
n = const_n
print ('n =', n, ' (Χρήση n = const_n)')
n[0] = n[0] + 10
n[1] = n[1] + 10
n[2] = n[2] + 10
print ('n + 10 =', n)
n = const_n
print ('n =', n)
