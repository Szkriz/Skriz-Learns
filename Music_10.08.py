import sys
from time import sleep
import time
from rich import print  

def printlyrics():
    lines = [
        ("du du du du", 0.15),
        ("Max Verstappen", 0.09),
        ("du du du du", 0.15),
        ("Max Verstappen", 0.09)
    ]
    
    delays = [0.5, 0.5, 0.09, 0.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(f"[grey78]{char}[/grey78]", end='')
            sys.stdout.flush()
            sleep(char_delay)
        print()  
        time.sleep(delays[i])

printlyrics()