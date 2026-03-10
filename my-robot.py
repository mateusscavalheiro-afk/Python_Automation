import pyautogui as py
import time as tm

py.FAILSAFE = True
py.alert("Alert: Don't use the computer")
tm.sleep(1)
py.press('win')
tm.sleep(1)
py.write('bloco', interval = 0.1)
tm.sleep(1)
py.press('enter')
tm.sleep(1)
py.write('Automacao Industrial', interval = 0.1)
tm.sleep(1)
py.moveTo(1124, 144)
tm.sleep(0.5)
py.click(1124, 144)
py.alert('Have a great day ;)')