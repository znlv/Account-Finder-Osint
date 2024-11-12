import subprocess
import sys
import time
import os 

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    if os.name == 'nt': 
        subprocess.run("cls", shell=True)
    else:    
        subprocess.run("clear", shell=True)
 
def startingmenu():
    slow_print("Our OSINT Tool is starting give it a moment.")
    time.sleep(0.5)
    clear()
    slow_print("Our OSINT Tool is starting give it a moment..")
    time.sleep(0.5)
    clear()
    slow_print("Our OSINT Tool is starting give it a moment...")
    clear()

def run():
    subprocess.run("python ./src/main.py", capture_output=True)


startingmenu()
