import pyautogui as py
import time as tm

py.alert("Calm down partner!")
tm.sleep(5)
position = py.position()
print(position)