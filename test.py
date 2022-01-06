# import pyautogui
import time
# import random

# time.sleep(2)

# for i in range(36):
#     print('run')
#     # pyautogui.press('num2')
#     pyautogui.press('num2')
#     time.sleep(random.randint(20,32))
#     pyautogui.press('num2')
#     wait = random.randint(30,60)
#     time.sleep(wait)
import ctypes

# Move cursor to x 500 and y 500
time.sleep(2)
ctypes.windll.user32.SetCursorPos(500,500)