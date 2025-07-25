import time
import os

text = "hehehehehe"
width = 100  # total width of the line

for i in range(width + 1):
    print("-" * i + text)
    time.sleep(0.09)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
