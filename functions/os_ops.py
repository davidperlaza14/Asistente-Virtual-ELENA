import os 
import subprocess as sp

paths = {
    'notepad': "/usr/bin/gedit",
    'google': "/usr/bin/gnome-www-browser",
    'calculator': "/usr/bin/gnome-calculator",
    'terminal': "/usr/bin/gnome-terminal",
    'pomodoro': "/usr/bin/gnome-pomodoro",
    'clocks': "/usr/bin/gnome-clocks",
    'camera': "cheese",
    'firefox': "/usr/bin/firefox"
}

def open_camera():
    os.system(paths['camera'])

def open_notepad():
    os.system(paths['notepad'])

def open_google():
    os.system(paths['google'])

def open_calculator():
    os.system(paths['calculator'])

def open_terminal():
    os.system(paths['terminal'])
    
def open_pomodoro():
    os.system(paths['pomodoro'])

def open_clocks():
    os.system(paths['clocks'])

def open_firefox():
    os.system(paths['firefox'])