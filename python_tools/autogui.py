import pyautogui
import time

for i in range (10):
	pyautogui.moveTo(100, 100, duration=0.25)
	time.sleep(2)
	pyautogui.moveTo(100, 200, duration=0.25)
	time.sleep(2)
	pyautogui.moveTo(200, 200, duration=0.25)
	time.sleep(2)
	pyautogui.moveTo(200, 100, duration=0.25)