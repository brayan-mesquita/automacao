import pyautogui, sys
import time as tm

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')






# def login(senha, ano):
#     pyautogui.PAUSE = 1
#     pyautogui.click(x=447, y=271)
#     pyautogui.PAUSE = 1.5
#     pyautogui.write('telnet 172.22.0.85 23', interval=0.07)
#     pyautogui.PAUSE = 1
#     pyautogui.hotkey('enter')
#     time.sleep(2)
#     pyautogui.write('sesdec', interval=0.02)
#     pyautogui.hotkey('enter')
#     pyautogui.PAUSE = 1.5
#     pyautogui.write('sesdec', interval=0.02)
#     pyautogui.hotkey('enter')
#     time.sleep(2)
#     pyautogui.write(ano, interval=0.02)
#     pyautogui.hotkey('enter')
#     time.sleep(2)
#     pyautogui.write('01606363298', interval=0.02)
#     time.sleep(2)
#     pyautogui.write(senha, interval=0.02)
#     pyautogui.hotkey('enter')
#     time.sleep(2)
#     pyautogui.hotkey('enter')