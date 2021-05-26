import ctypes
user32 = ctypes.WinDLL('user32', use_last_error=True)
print (user32.GetForegroundWindow())
