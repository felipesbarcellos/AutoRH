import pyautogui as p
from time import sleep

p.PAUSE = 1

class Inicializador():
    def __init__(self):
        self.conta = str(input('Login: '))
        self.senha = 'Robotomono123!'

    def abre_chrome(self):
        p.click(26, 753)
        p.typewrite('chrome')
        p.press('enter')
        p.hotkey('win', 'right')
        print('Chrome foi aberto com sucesso!')

    def troca_janela(self):
        with p.hold('alt'):
            p.press('tab')

    def abre_portal(self):
        p.click(1000,0)
        p.hotkey('ctrl', 'l')
        p.typewrite('chiapetta/PortalRH/')
        p.press('enter')
        print('Portal Aberto')

    def loga_portal(self):
        p.click(909,231)
        p.typewrite(self.conta)
        p.press('tab')
        p.typewrite(self.senha)
        p.press('enter')
        sleep(10)
        p.press('home')
        print('Logado com Sucesso')

    def aba_solicitacao(self):
        p.click(714,115)
        p.click(720,530)
        sleep(5)
        p.press('home')
        p.click(863,323)
        p.press('down')
        p.press('enter')
        sleep(160)
        p.press('home')
        p.click(754,441)
        sleep(160)

def iniciar():
    i = Inicializador()
    i.abre_chrome()
    i.abre_portal()
    i.loga_portal()
    i.aba_solicitacao()


if __name__ == '__main__':
    iniciar()
