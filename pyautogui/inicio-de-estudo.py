import pyautogui as pg
import time as tm

 
tm.sleep(3)
pg.hotkey('ctrl', 'space')
tm.sleep(0.5)
pg.write('freeplane', interval=0.02)
pg.hotkey('enter')
tm.sleep(0.5)
pg.hotkey('winleft', 'left')
tm.sleep(0.4)
pg.press('down', presses=1)
tm.sleep(0.5)
pg.hotkey('end')
tm.sleep(0.5)
pg.hotkey('enter')
tm.sleep(5)
pg.hotkey('winleft', 'left')

#pomodoro
pg.hotkey('ctrl', 'space')
tm.sleep(0.4)
pg.write('pomodo', interval=0.02)
tm.sleep(0.4)
pg.hotkey('enter')
pg.hotkey('winleft', 'shift', 'right')
pg.click(x=1500, y=500)
tm.sleep(0.4)

#mudar janela
pg.hotkey('winleft', 'alt', 'down')
tm.sleep(0.4)
pg.hotkey('ctrl', 'space')

pg.write('planilhas', interval=0.02)
tm.sleep(0.4)
pg.hotkey('enter')
tm.sleep(0.4)
pg.hotkey('winleft', 'shift', 'right')