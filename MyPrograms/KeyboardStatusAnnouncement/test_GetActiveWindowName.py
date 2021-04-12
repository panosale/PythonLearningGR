import win32gui
w = win32gui
last_window = w.GetWindowText (w.GetForegroundWindow())
print (last_window)
while True:
    if last_window != w.GetWindowText(w.GetForegroundWindow()):
        print (w.GetWindowText(w.GetForegroundWindow()))
        last_window = w.GetWindowText (w.GetForegroundWindow())
