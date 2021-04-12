import win32api,win32con
caps_status = win32api.GetKeyState(win32con.VK_CAPITAL)
if caps_status==0:
    print('CapsLock is OFF')
else:
    print('CapsLock is ON')
