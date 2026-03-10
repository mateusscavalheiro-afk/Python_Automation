import pyautogui as py
import time as tm

#First step: Open the Windows Menu
py.press('Win')
tm.sleep(3)
py.write('bloco', interval = 0.1)
py.press('Enter')