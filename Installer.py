import webbrowser
import sys, subprocess, random, json, asyncio, os, time
try:
    import colorama, pyfade, discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord'])
from colorama import Fore
from datetime import datetime
from discord.ext import commands
import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# Example

while True:
    for i in range(1, 100):
        print('\n')
    print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, '''     ▄████▄   ▄▄▄        ██████ ▄▄▄█████▓
    ▒██▀ ▀█  ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒
    ▒▓█    ▄ ▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░
    ▒▓▓▄ ▄██▒░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ 
    ▒ ▓███▀ ░ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ 
    ░ ░▒ ▒  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   
    ░  ▒     ▒   ▒▒ ░░ ░▒  ░ ░    ░    
    ░          ░   ▒   ░  ░  ░    ░      
    ░ ░            ░  ░      ░           
    ░                                    '''))
    for i in range(1, 8):
        print('\n')
    print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_red, """This is the OFFICIAL installer for the Cast Scanner. Choose from the options below


    [1] Copy github to clipboard    [2] Proceed to install Cast Scanner    [3] Not Complete\n\n"""))
    choice1 = input('\nInput: ')
    if choice1 == '1':
        addToClipBoard('https://github.com/EllaTheScreensharer/Cast')

    if choice1 == '2':
        webbrowser.open('https://anonfiles.com/TbVfM0keyc/Cast_exe')
