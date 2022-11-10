#importando
from pyautogui import click, press, hotkey, locateOnScreen, moveTo, moveRel, confirm, typewrite, doubleClick, tripleClick, dragTo
from time import sleep
import pyperclip

#pausa contra os bugs


#classe
class Controle():
    def __init__(self):
        self.loaded = 'assets/loaded.png'
        self.numero = 'assets/numero.png'
        self.observacao = 'assets/obs.png'
        self.download = 'assets/clique.png'
        self.salvar = 'assets/salvar.png'
        self.sheets = 'assets/sheets.png'
        self.nomecapacitacao = 'assets/nome.png'
        self.datainicio = 'assets/datainicio.png'
        self.data = 'assets/datarecebimento.png'
        self.cargahoraria = 'assets/cargahoraria.png'
        self.drive = 'assets/drive.png'
    
    #função APROVAÇÂO
    def finaliza_solicitacao_aprova(self):
        confirm(text='Solicitação finalizada?', title='Continuar', buttons=['OK'])
        click(1000,0)
        press('end')
        click(757,572) #BOTÃO APROVA
        sleep(5)
        hotkey('ctrl','w')
        sleep(1)
        press('tab')
        sleep(1)

    #função REPROVAÇÂO
    def finaliza_solicitacao_reprova(self):
        confirm(text='Solicitação finalizada?', title='Continuar', buttons=['OK'])
        sleep(1)
        click(843,579) #BOTÃO REPROVA
        sleep(3)
        hotkey('ctrl','w')
        sleep(5)
        press('tab')
        sleep(1)
    
    #função que abre a solicitação
    #a partir de uma lista de solicitações
    def abre_solicitacao(self):
            click(1000,0)
            hotkey('ctrl', 'enter')
            sleep(0.5)
            hotkey('ctrl', 'tab')
            sleep(1)
            
            carregado = False
            while carregado == False:
                sleep(3)
                if (locateOnScreen(self.loaded, grayscale=True)) != None:
                    carregado = True
                    break
                else:
                    press('esc')
                    press('f5')       
            carregado = False

##          while True:
##              sleep(3)
##              try:
##                  loaded = locateOnScreen(self.loaded, grayscale=True)
##                  if loaded == None:
##                      raise ReferenceError
##                  else:
##                      break
##                  
##              except ReferenceError:
##                  press('esc')
##                  press('f5')
##                  pass
            
            moveTo(locateOnScreen(self.data))
            moveRel(0,20)
            tripleClick()
            hotkey('ctrl', 'c')
            self.recebimento = pyperclip.paste()
            
            moveTo(738,404,0.1)
            doubleClick()
            hotkey('ctrl', 'c')
            self.num = pyperclip.paste()

            moveTo(locateOnScreen(self.nomecapacitacao))
            moveRel(0,20)
            tripleClick()
            hotkey('ctrl', 'c')
            self.nome = pyperclip.paste()
            press('pgdn')

            moveTo(locateOnScreen(self.datainicio))
            moveRel(0,20)
            tripleClick()
            hotkey('ctrl', 'c')
            self.inicio = pyperclip.paste()
            
            moveTo(locateOnScreen(self.cargahoraria))
            moveRel(-10,20)
            doubleClick()
            hotkey('ctrl', 'c')
            self.ch = pyperclip.paste()
            
            while carregado == False:
                if (locateOnScreen(self.download, grayscale=True)) != None:
                    carregado = True
                    click(locateOnScreen(self.download, grayscale=True))
                    pass
                else:
                    print('Não localizado')
                    sleep(2)
            carregado = False
            
            sleep(2)
            
            while carregado == False:
                if (locateOnScreen(self.salvar, grayscale=True)) != None:
                    typewrite(self.num)
                    press('enter')
                    carregado = True
                    pass
                else:
                    print('Não localizado')
                    sleep(2)
            carregado = False
            
            moveTo(750, 700, 0.2)
            sleep(4)
            dragTo(697, 25, 1, button='left')

    def abrir_planilha(self):
        while True:
                try:
                    self.planilha = locateOnScreen(self.sheets)
                    if self.planilha == None:
                        raise ReferenceError
                    click(self.planilha)
                    break
                except ReferenceError:
                    print('Não localizado')
                    sleep(3)
                    continue
##        hotkey('shift', 'alt', 'k')
##        if self.situacao == 'Aprovar lista':
##            while True:
##                try:
##                    self.planilha_aprova_lista = locateOnScreen('assets/planilha_aprova_lista.png')
##                    if self.planilha_aprova_lista == None:
##                        raise ReferenceError
##                    click(self.planilha_aprova_lista)
##                    break
##                except ReferenceError:
##                    print('Não localizado')
##                    sleep(3)
##                    press('esc')
##                    break
##        elif self.situacao == 'Reprovar lista':
##            while True:
##                try:
##                    self.planilha_reprova_lista = locateOnScreen('assets/planilha_reprova_lista.png')
##                    if self.planilha_reprova_lista == None:
##                        raise ReferenceError
##                    click(self.planilha_reprova_lista)
##                    break
##                except ReferenceError:
##                    print('Não localizado')
##                    sleep(3)
##                    press('esc')
##                    break
#APROVA LISTA
    def escreve_mensagem(self):
        self.situacao = confirm(text='Avalie a lista que foi aberta pelo programa.', title='Avaliar solicitação', buttons=['Aprovar lista', 'Reprovar lista', 'Aprovar certificado', 'Reprovar certificado', 'Aprovar avaliação' ,'Reprovar avaliação'])
        click(1000,0)
        hotkey('ctrl','w')
        hotkey('ctrl','tab')
        press('end')
        if self.situacao == 'Aprovar lista':
            press('pagedown')
            press('pagedown')
            moveTo(locateOnScreen('assets/obs.png',grayscale=True))
            moveRel(0, 50)
            click()
            pyperclip.copy("""Prezado(a),
 
Agradecemos o envio da lista de presença. Em breve faremos a inclusão/importação da capacitação nos sistema Metadados e SA.
 
Atenciosamente,
Treinamento e Desenvolvimento.
""")
            hotkey('ctrl', 'v')
            self.tipo = confirm(text='Qual o Tipo de Treinamento?', title='Tipo de capacitação', buttons=['Inicial', 'Periódico', 'Reciclagem', 'Eventual'])
            self.abrir_planilha()
            sleep(1)
            hotkey('alt', 'i')
            sleep(1)
            press('r')
            sleep(1)
            press('b')
            sleep(1)
            hotkey('ctrl', 'left')
            typewrite(self.tipo)
            press('tab')
            typewrite(self.num)
            press('tab')
            typewrite(self.nome)
            press('tab');press('enter');press('down');press('tab')
            press('tab');press('tab')
            typewrite(self.inicio) #definir
            press('tab')
            typewrite(self.recebimento) #definir
            press('tab')
            typewrite(self.ch) #definir
            click(locateOnScreen(self.drive))
            moveTo(717, 704, 0.2)
            sleep(1)
            dragTo(432, 206, 1, button='left')
            self.finaliza_solicitacao_aprova()


#REPROVA LISTA
        elif self.situacao == 'Reprovar lista':
            press('pagedown')
            press('pagedown')
            moveTo('assets/obs.png')
            moveRel(0, 50)
            click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio da lista de presença, porém só conseguiremos realizar a inclusão/importação da capacitação nos sistemas Metadados e SA se recebermos até o dia: __/__/____ ( 2 dias úteis após a reprovação) as informações abaixo que não constam no documento em anexo. São elas:
Objetivo;
Tipo de treinamento/capacitação;
Conteúdo programático.


Atenciosamente,
Treinamento e Desenvolvimento
""")
            hotkey('ctrl', 'v')
            #self.abrir_planilha()
            sleep(1)
            press('down')
            sleep(1)
            hotkey('alt', 'i')
            sleep(1)
            press('r')
            sleep(1)
            press('b')
            sleep(1)
            hotkey('ctrl', 'left')
            typewrite(self.num)
            press('tab')
            typewrite(self.nome)
            press('tab')
            typewrite(self.inicio)



#APROVA CERTIFICADO
        elif self.situacao == 'Aprovar certificado':
            press('pagedown')
            press('pagedown')
            moveTo('assets/obs.png')
            moveRel(0, 50)
            click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio do certificado. Em breve faremos a inclusão/importação da capacitação nos sistema Metadados e SA.

Atenciosamente,
Treinamento e Desenvolvimento""")
            hotkey('ctrl', 'v')
            self.finaliza_solicitacao_aprova()


#REPROVA CERTIFICADO
        elif self.situacao == 'Reprovar certificado':
            press('pagedown')
            press('pagedown')
            moveTo('assets/obs.png')
            moveRel(0, 50)
            click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio do Certificado, porém só conseguiremos realizar a inclusão/importação no sistemas Metadados se recebermos as informações abaixo que não constam no documento em anexo. 
São elas:
Data de Início e Conclusão do Curso;
Carga Horária total do Curso.

Atenciosamente,
Treinamento e Desenvolvimento""")
            hotkey('ctrl', 'v')
            self.finaliza_solicitacao_reprova()


#APROVA AVALIAÇÃO
        elif self.situacao == 'Aprovar avaliação':
            press('pagedown')
            press('pagedown')
            moveTo('assets/obs.png')
            moveRel(0, 50)
            click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio da avaliação de eficácia. Em breve faremos a inclusão da mesma no sistema Metadados.
No caso de dúvidas ou orientações, retornaremos o contato.

Atenciosamente,
Treinamento e Desenvolvimento
""")
            hotkey('ctrl', 'v')
            self.finaliza_solicitacao_aprova()


#REPROVA AVALIAÇÃO
        elif self.situacao == 'Reprovar avaliação':
            press('pagedown')
            press('pagedown')
            moveTo('assets/obs.png')
            moveRel(0, 50)
            click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio da avaliação de eficácia. Porém só conseguiremos fazer a inclusão no sistema Metadados se a solicitação estiver conforme a IT DRH 0109.006 Metodologia De Avaliação De Eficácia disponível na Intranet.

Atenciosamente,
Treinamento e Desenvolvimento
""")
            hotkey('ctrl', 'v')
            self.finaliza_solicitacao_reprova()

            
