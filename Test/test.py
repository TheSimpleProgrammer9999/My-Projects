#import ctypes
#SPI_SETDESKWALLPAPER = 20 
#ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "rick-roll.jpg" , 0)
import atexit 
from time import*
from pyautogui import press
import psutil
def is_process_running(name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == name:
            return True
    return False
for i in range(10):
    print("ahh")
    sleep(1)
if is_process_running('script.py'):
    print('The script is running.')
else:
    print('The script is not running.')