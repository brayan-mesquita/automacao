import pyautogui as pg
import time as tp

def pesquisar(tombo):
    pg.click(x=395, y=13)
    pg.hotkey('ctrl', 'f')
    pg.write(tombo)
    pg.hotkey('enter')

#pesquisar('diaria')

# unidade = pg.prompt(text='Unidade-Departamento', title='Lançamentos', default='')
# lista = pg.prompt(text='Tombos ex: 11111-22222', title='Lançamentos', default='')
# lista_ = lista.split("-")
# unidade_ = unidade.split("-")


#pg.click(x=30, y=1029)
lista = ['casa', 'catha']
print(lista[0].upper())







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