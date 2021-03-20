import sys
import re
import win32api as win32
import win32con
from time import sleep


def rotate_screen(direction=0):
    device = win32.EnumDisplayDevices(None, 0)

    if direction==0:
        rotation_val = win32con.DMDO_DEFAULT
    elif direction==1:
        rotation_val = win32con.DMDO_90
    elif direction==2:
        rotation_val = win32con.DMDO_180
    elif direction==3:
        rotation_val = win32con.DMDO_270


    dm = win32.EnumDisplaySettings(
        device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
    if((dm.DisplayOrientation + rotation_val) % 2 == 1):
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    dm.DisplayOrientation = rotation_val

    win32.ChangeDisplaySettingsEx(device.DeviceName, dm)
while True:
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    rotate_screen(0)
    sleep(2)
    rotate_screen(1)
    sleep(2)
    rotate_screen(2)
    sleep(2)
    rotate_screen(3)
    sleep(2)
    rotate_screen(0)