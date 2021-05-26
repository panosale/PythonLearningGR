print ('***** user32 **************************************')
import ctypes
user32 = ctypes.WinDLL('user32', use_last_error=True)
handle = user32.GetForegroundWindow()
threadid = user32.GetWindowThreadProcessId(handle, 0)   # Get the thread id from that window handle
layout_id = user32.GetKeyboardLayout(threadid)          # Get the keyboard layout id from the threadid
print (handle)
print (threadid)
print ('***** kernel32 **************************************')
#kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
#def_layout_id = kernel32.GetSystemDefaultUILanguage()
#def_language_id = def_layout_id & (2 ** 16 - 1)
#language_id_hex = hex(def_language_id)
#print (def_layout_id)
#print (language_id_hex)
print ('***** py_win_keyboard_layout **************************************')
import py_win_keyboard_layout
print (hex(py_win_keyboard_layout.get_foreground_window_keyboard_layout() & (2 ** 16 - 1)))
print ('***** win32gui, win32con **************************************')
import win32gui, win32api
print (win32gui.GetForegroundWindow())
print (hex(win32api.GetKeyboardLayout() & (2 ** 16 - 1)))