import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\Stpus\\AppData\\Local\\Discord\\Update.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'edge': "C:\\ProgramData\\Microsoft\\Windows\Start Menu\\Programs\\Microsoft Edge.lnk",
    'tidal':"C:\\Users\\Stpus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\TIDAL Music AS\\TIDAL.lnk",
    'cmd': "C:\\Users\\Stpus\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
}


#Open programs 
def abre_camara():
    sp.run('star microsoft.windows.camera:', shell=True)

def abre_notas():
    os.startfile(paths['notepad'])


def abre_discord():
    os.startfile(paths['discord'])
    

def abre_edge():
    os.startfile(paths['edge'])


def tidal():
    os.startfile(paths['tidal'])

def cmd():
    os.startfile(paths['cmd'])

def calculadora():
    sp.Popen(paths['calculator'])