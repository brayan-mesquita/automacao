import pyautogui, time
#senha
senha = pyautogui.password(text='Senha de acesso:', title='Usuario Brayan', default='', mask='*')
#login
def login(senha, ano):
    pyautogui.PAUSE = 1
    pyautogui.click(x=447, y=271)
    pyautogui.PAUSE = 1.5
    pyautogui.write('telnet 172.22.0.85 23', interval=0.07)
    pyautogui.PAUSE = 1
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.write('sesdec', interval=0.02)
    pyautogui.hotkey('enter')
    pyautogui.PAUSE = 1.5
    pyautogui.write('sesdec', interval=0.02)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.write(ano, interval=0.02)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.write('01606363298', interval=0.02)
    time.sleep(2)
    pyautogui.write(senha, interval=0.02)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('enter')

def detaconta(conta):
    time.sleep(2)
    pyautogui.write(conta, interval=0.02)


#janela 
while True:
    opcao = pyautogui.prompt(text="Fechar='0'\nLogin='Ano 19, 20...'\n---------------\nDetalhaConta='dc' " , title='SIAFEM' , default='')
    if opcao == '0':
        break
    elif opcao == '20':
        login(senha, '2020')
    elif opcao == '19':
        login(senha, '2019')
    elif opcao == 'dc':
        conta = pyautogui.prompt(text='Conta:', title='Informe a conta')
        detaconta(str(conta))
        time.sleep(1.5)
        pyautogui.hotkey('enter')



   
