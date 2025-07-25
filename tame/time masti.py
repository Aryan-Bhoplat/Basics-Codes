'''
import time 
for i in range(5):
    print("\r" + " " * i + "/",end = " ",flush=True)
    time.sleep(0.1)

'''

import time
symbols = ['/','-','\\','|']
for i in range(50):
    symbol = symbols[i % len(symbols)]
    print("\r"+" "*i+symbol,end="",flush=True)
    time.sleep(0.09)


