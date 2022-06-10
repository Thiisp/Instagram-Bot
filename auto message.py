import pyautogui
from time import sleep

pyautogui.PAUSE = 0.3


pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.click(x=-23, y=49)
pyautogui.click(x=-140, y=129)
pyautogui.click(x=-999, y=48)
pyautogui.write('instagram.com')
pyautogui.press('enter')
sleep(1.5)
pyautogui.click(x=-497, y=296)
pyautogui.write('username') # aqui você troca o username.
pyautogui.click(x=-498, y=341)
pyautogui.write('password') # aqui você coloca sua senha.
pyautogui.click(x=-483, y=394)
sleep(4)
pyautogui.click(x=-703, y=490)
sleep(2)
pyautogui.click(x=-696, y=553)
pyautogui.click(x=-856, y=48)
pyautogui.write('https://www.instagram.com/thiisp/')
pyautogui.press('enter')
sleep(4)
pyautogui.click(x=-672, y=214)
sleep(4)

count = 0

while count <= 10000:
    pyautogui.write('Bot Automatico de mandar msg Instagram.')
    pyautogui.press('enter')
