import ctypes
import py_win_keyboard_layout
user32 = ctypes.WinDLL('user32', use_last_error=True)
handle = user32.GetForegroundWindow()
threadid = user32.GetWindowThreadProcessId(handle, 0)   # Get the thread id from that window handle
layout_id = user32.GetKeyboardLayout(threadid)          # Get the keyboard layout id from the threadid

#kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
#def_layout_id = kernel32.GetSystemDefaultUILanguage()
#def_language_id = def_layout_id & (2 ** 16 - 1)
#language_id_hex = hex(def_language_id)

print (handle)
print (threadid)
#print (def_layout_id)
#print (language_id_hex)