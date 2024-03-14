import pyautogui
import os
path=r'C:\Users\Administrator\Desktop\img\text.png'
position=pyautogui.locateCenterOnScreen(path,confidence=0.7)
# pyautogui.moveTo(position)
pyautogui.click(position.x,position.y,2)
print(position)