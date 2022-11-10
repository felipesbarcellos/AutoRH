from pyautogui import *

class Teste:
    def __init__(self):
        self.botao_selecionado = 'teste_assets/botao_selecionado.png'
        self.numero = 'teste_assets/numero.png'

    def entra_solicitacao(self):
        while True:
            
            try:
                botao = locateOnScreen(self.botao_selecionado)
                if botao == None:
                    raise Exception
                
                hotkey('ctrl','enter')
                hotkey('ctrl','tab')
                break

            except:
                press('tab')
                sleep(0.1)
                continue

    def copia_numero(self):
        while True:
            try:
                numero = locateOnScreen(self.numero)
                if numero == None:
                    sleep(10)
                    raise Exception

                moveTo(numero)
                moveRel(0,20)
                doubleClick()
                hotkey('ctrl','c')
                break

            except:
                press('esc')
                press('f5')
                continue
