# Total memory used by Python process?
# Από: https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)  # in bytes 
