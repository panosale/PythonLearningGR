import win32gui
i = 1
w = win32gui
last_window = w.GetWindowText (w.GetForegroundWindow())
print (i, last_window)
while i < 10000000:
    if last_window != w.GetWindowText(w.GetForegroundWindow()):
        print (i, w.GetWindowText(w.GetForegroundWindow()))
        last_window = w.GetWindowText (w.GetForegroundWindow())
    i += 1