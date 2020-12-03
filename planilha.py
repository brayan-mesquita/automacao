import pyautogui as pg
import time as tp

unidade = pg.prompt(text='Unidade-Departamento', title='Lançamentos', default='')
lista = pg.prompt(text='Tombos ex: 11111-22222', title='Lançamentos', default='')

#variáveis a serem usadas
lista_ = lista.split("-")
unidade_ = unidade.split(",")

def pesquisar(tombo):
    pg.click(x=390, y=13)
    tp.sleep(1)
    pg.hotkey('ctrl', 'f')
    tp.sleep(1)
    pg.write(tombo, interval=0.02)
    pg.hotkey('enter')
    pg.click(x=30, y=1029)
def encontrado(unidade, departamento):
    tp.sleep(2)
    pg.press('right', presses=3)
    pg.write(unidade.upper(), interval=0.02)
    pg.hotkey('tab')
    pg.write(departamento.upper(), interval=0.02)
    pg.hotkey('tab')
    pg.press('right', presses=1)
    pg.write('SIM')
    pg.click(x=390, y=13)
def novo(tombo, unidade, departamento):
    tp.sleep(1.5)
    pg.write(tombo, interval=0.02)
    pg.press('right', presses=3)
    pg.write(unidade, interval=0.02)
    pg.hotkey('tab')
    pg.write(departamento, interval=0.02)
    pg.hotkey('tab')
    pg.press('right', presses=1)
    pg.write('NR')
    pg.click(x=390, y=13)

total_tombos = len(lista_)
#janela 
x = 0
if x <= len(lista_):
    for i in lista_:
        opcao= pg.confirm(text='Pesquisar tombo: {}'.format(lista_[x]), title='Total tombos a pesquisar {}'.format(total_tombos), buttons=['Pesquisar', 'Cancelar'])
        if opcao == 'Cancelar':
            break
        elif opcao == 'Pesquisar':
            pesquisar(i)
            pergunta = pg.confirm(text='Colar', buttons=['Sim', 'Novo', 'Cancelar'])
            if pergunta == 'Sim':
                encontrado(unidade_[0], unidade_[1])
                x += 1
                total_tombos = total_tombos -1
            elif pergunta == 'Cancelar':
                break
            elif pergunta == 'Novo':
                novo(lista_[x], unidade_[0], unidade_[1])
                x += 1
                total_tombos = total_tombos -1
        
            



   
