import sys
import re
from time import sleep
import pygetwindow
from random import randint

while True:
    try:
        win = pygetwindow.getWindowsWithTitle('Device Manager')[0]
        win.size = (randint(200, 900), randint(200,1200))
        win.moveTo(randint(0, 1920), randint(0, 1080))

    except Exception as e:
        print(e)

    try:
        win = pygetwindow.getWindowsWithTitle('System Information')[0]
        win.size = (randint(200, 900), randint(200,1200))
        win.moveTo(randint(0, 1920), randint(0, 1080))
        
    except Exception as e:
        print(e)
    sleep(0.3)
