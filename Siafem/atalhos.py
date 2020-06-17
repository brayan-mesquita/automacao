import pyautogui
senha = 'xxx'
#senha
while senha != 'senha':
    senha = pyautogui.password(text='Senha de acesso:', title='Usuario Brayan', default='', mask='*')
    if senha == '0':
        break
#escolha ano
ano = pyautogui.prompt(text="Exercício: 18, 19, 20-Enter..." , title='Ano para conculta' , default='')
if ano == '18':
    ano = '2018'
elif ano == '19':
    ano = '2019'
else:
    ano = '2020'
#login
pyautogui.PAUSE = 1
pyautogui.click(x=447, y=271)
pyautogui.PAUSE = 1
pyautogui.write(ano, interval=0.01)

#janela teimosa
while True:
    opcao = pyautogui.prompt(text="Fechar='0'\nLogin='1'\n---------------\nLançar NE='lne'\nCons NE='cne'\n---------------\nDetalhaConta='dc' " , title='SIAFEM' , default='')
    if opcao == '0':
        break
    elif opcao == '1': #login de novo
        pyautogui.PAUSE = 1
        pyautogui.click(x=447, y=271)
        pyautogui.PAUSE = 1
        pyautogui.write('2020', interval=0.02)
    elif opcao == 'lne':
        pyautogui.PAUSE = 1
        pyautogui.click(x=447, y=271)
        pyautogui.PAUSE = 1
        pyautogui.write('sesdec', interval=0.02)
        pyautogui.hotkey('enter')
        pyautogui.write('sesdec', interval=0.02)
        pyautogui.hotkey('enter')
        pyautogui.write('15003', interval=0.02)
        pyautogui.hotkey('enter')
        pyautogui.write('0000001', interval=0.02)
        pyautogui.hotkey('tab')
        pyautogui.write('sesdec', interval=0.02)
        pyautogui.hotkey('tab')
        pyautogui.write('sesdec', interval=0.02)
        pyautogui.hotkey('enter')
        pyautogui.PAUSE = 1
    elif opcao == 'dc':
        conta = pyautogui.prompt(text="Ex.: xxxxxx-DEZ" , title='Conta e Mês separado por -', default='')
        pyautogui.PAUSE = 1.2
        pyautogui.click(x=447, y=271)
        pyautogui.PAUSE = 1
        pyautogui.write(conta, interval=0.01)


   
