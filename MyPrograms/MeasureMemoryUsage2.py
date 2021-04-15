# Μέτρηση χρήσης μνήμης κατά την εκτέλεση ενός προγράμματος python με τη χρήση της βιβλιοθήκης resource
# 2ος τρόπος με λιγότερη κατανάλωση πόρων.
# Από: https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba

# First — we define a class to perform the memory monitoring
import resource

from time import sleep

class MemoryMonitor:
    def __init__(self):
        self.keep_measuring = True

    def measure_usage(self):
        max_usage = 0
        while self.keep_measuring:
            max_usage = max(
                max_usage,
                resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            )
            sleep(0.1)

        return max_usage

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    monitor = MemoryMonitor()
    mem_thread = executor.submit(monitor.measure_usage)
    try:
        fn_thread = executor.submit(ΠΡΟΓΡΑΜΜΑ ΠΟΥ ΘΕΛΟΥΜΕ ΝΑ ΕΛΕΓΞΟΥΜΕ)
        result = fn_thread.result()
    finally:
        monitor.keep_measuring = False
        max_usage = mem_thread.result()
        
    print(f"Peak memory usage: {max_usage}")
    
