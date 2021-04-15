# Μέτρηση χρήσης μνήμης κατά την εκτέλεση ενός προγράμματος python με τη χρήση της βιβλιοθήκης resource.
# 1ος τρόπος με περισσότερη κατανάλωση πόρων.
# Από: https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba

import tracemalloc

tracemalloc.start()
my_complex_analysis_method()  # <--- ΤΟ ΟΝΟΜΑ ΤΗΣ ΣΥΝΑΡΤΗΣΗΣ ΜΑΣ
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
