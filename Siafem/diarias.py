import pyautogui
lancamentos = int(input('lançamentos: '))
evento = str(input('Digite 1 - Em analise; 2 - A homologar; 3 - Homologada ex. atual; 4 - A homologar ex. anterior: '))
if evento == "1":
    evento = '540869'
    classi = '332110101'
elif evento == '2':
    evento = '540870'
    classi = '897110704'
elif evento == '3':
    evento = '540871'
    classi = '897110705'
elif evento == '4':
    evento = '540879'
    classi = '897110706'
cpfs = input("Digite CPF separando por '-': ")
cpf_list = cpfs.split("-")
fonte = str(input('Digite 1 para fonte - 0100000000; 3 - 0300000000: '))
if fonte == '1':
    fonte = '0100000000'
if fonte == '3':
    fonte = '0300000000'
valor = str(input('valor: '))

i = 0
pyautogui.click(x=395, y=13)
while i < lancamentos:
    pyautogui.write(evento)
    pyautogui.write(cpf_list[i])
    pyautogui.hotkey('tab')
    pyautogui.write(classi)
    pyautogui.hotkey('tab')
    pyautogui.write(fonte)
    pyautogui.write(valor)
    pyautogui.hotkey('tab')
    i += 1
