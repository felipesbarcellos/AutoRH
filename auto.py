import pyperclip
import pyautogui as p
from time import time, sleep

#Classe
class Auto:
    #Construtor
    def __init__(self):
        self.loaded = 'assets/loaded.png'
        self.numero = 'assets/numero.png'
        self.observacao = 'assets/obs.png'
        self.download = 'assets/clique.png'
        self.salvar = 'assets/salvar.png'
        self.botao_s = 'assets/botao_s.png'
        self.botao_us = 'assets/botao_us.png'

    #Seleciona primeira solicitação
    def seleciona_primeira_solicitacao(self):
        p.click(1000,0)
        while True:
            try:
                botao = p.locateOnScreen(self.botao_s)
                if botao == None:
                    raise ReferenceError
            except ReferenceError:
                p.press('tab')
                continue

    #Abre a solicitação
    def abre_solicitacao(self):
        sleep(2)
        try:
            botao_s = p.locateOnScreen(self.botao_s)
            if botao_s == None:
                raise ReferenceError
            p.hotkey('ctrl','enter')
            p.hotkey('ctrl','tab')
        except ReferenceError:
            print('Erro: abre_solicitacao()')
            sleep(2)

    #Espera a página da solicitação carregar, se não carregar: atualiza
    def espera(self):
        while True:
            try:
                sleep(2)
                carregado = p.locateOnScreen(self.loaded, grayscale=True)
                if carregado == None:
                    raise ReferenceError
                break
            except ReferenceError:
                print('Página da solicitação não carregou. Tentando novamente...')
                p.press('esc')
                p.press('f5')
                sleep(2)
                continue

    #Copia número de solicitação
    def copia_numero(self):
        while True:
            try:
                sleep(2)
                numero = p.locateOnScreen(self.numero, grayscale=True)
                if numero == None:
                    raise ReferenceError
                p.moveTo(numero)
                p.moveRel(0,20)
                p.doubleClick()
                p.hotkey('ctrl','c')
                break
            except ReferenceError:
                sleep(2)
                continue

    def baixa_pdf(self):
        while True:
            sleep(2)
            try:
                baixar = p.locateOnScreen(self.download, grayscale=True)
                if baixar == None:
                    raise ReferenceError
                p.click(baixar)
                while True:
                    try:
                        salvar = p.locateOnScreen(self.salvar, grayscale=True)
                        if salvar == None:
                            raise ReferenceError
                        p.hotkey('ctrl','v')
                        p.press('enter')
                        break
                    except ReferenceError:
                        sleep(3)
                        continue
                break
            except ReferenceError:
                p.press('pagedown')
                sleep(2)
                continue

    def abre_pdf(self):
        p.moveTo(750, 700, 0.2)
        sleep(10)
        p.dragTo(697, 25, 1, button='left')

#Escreve mensagem
    def escreve_mensagem(self):
        self.situacao = p.confirm(text='Avalie a lista que foi aberta pelo programa.', title='Avaliar solicitação', buttons=['Aprovar lista', 'Reprovar lista', 'Aprovar certificado', 'Reprovar certificado', 'Aprovar avaliação' ,'Reprovar avaliação'])
        sleep(1)
        p.hotkey('ctrl','w')
        sleep(1)
        p.hotkey('ctrl','tab')
        sleep(1)
        p.press('end')

#Aprova Lista
        if self.situacao == 'Aprovar lista':
            p.press('pagedown')
            p.press('pagedown')
            p.moveTo(p.locateOnScreen('assets/obs.png',grayscale=True))
            p.moveRel(0, 50)
            p.click()
            pyperclip.copy("""Prezado(a),
 
Agradecemos o envio da lista de presença. Em breve faremos a inclusão/importação da capacitação nos sistema Metadados e SA.
 
Atenciosamente,
Treinamento e Desenvolvimento.
""")
            p.hotkey('ctrl', 'v')
            self.finaliza_solicitacao_aprova()


#Reprova Lista
        elif self.situacao == 'Reprovar lista':
            p.press('pagedown')
            p.press('pagedown')
            p.moveTo('assets/obs.png')
            p.moveRel(0, 50)
            p.click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio da lista de presença, porém só conseguiremos realizar a inclusão/importação da capacitação nos sistemas Metadados e SA se recebermos até o dia: __/__/____ ( 2 dias úteis após a reprovação) as informações abaixo que não constam no documento em anexo. São elas:
Objetivo;
Tipo de treinamento/capacitação;
Conteúdo programático.


Atenciosamente,
Treinamento e Desenvolvimento
""")
            p.hotkey('ctrl', 'v')
            self.finaliza_solicitacao_reprova()


#Aprova Certificado
        elif self.situacao == 'Aprovar certificado':
            p.press('pagedown')
            p.press('pagedown')
            p.moveTo('assets/obs.png')
            p.moveRel(0, 50)
            p.click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio do certificado. Em breve faremos a inclusão/importação da capacitação nos sistema Metadados e SA.

Atenciosamente,
Treinamento e Desenvolvimento""")
            p.hotkey('ctrl', 'v')
            self.finaliza_solicitacao_aprova()


#Reprova Certificado
        elif self.situacao == 'Reprovar certificado':
            p.press('pagedown')
            p.press('pagedown')
            p.moveTo('assets/obs.png')
            p.moveRel(0, 50)
            p.click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio do Certificado, porém só conseguiremos realizar a inclusão/importação no sistemas Metadados se recebermos as informações abaixo que não constam no documento em anexo. 
São elas:
Data de Início e Conclusão do Curso;
Carga Horária total do Curso.

Atenciosamente,
Treinamento e Desenvolvimento""")
            p.hotkey('ctrl', 'v')
            self.finaliza_solicitacao_reprova()


#Aprova Avaliação
        elif self.situacao == 'Aprovar avaliação':
            p.press('pagedown')
            p.press('pagedown')
            p.moveTo('assets/obs.png')
            p.moveRel(0, 50)
            p.click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio da avaliação de eficácia. Em breve faremos a inclusão da mesma no sistema Metadados.
No caso de dúvidas ou orientações, retornaremos o contato.

Atenciosamente,
Treinamento e Desenvolvimento
""")
            p.hotkey('ctrl', 'v')
            self.aprovar()


#Reprova Avaliação
        elif self.situacao == 'Reprovar avaliação':
            p.press('pagedown')
            p.press('pagedown')
            p.moveTo('assets/obs.png')
            p.moveRel(0, 50)
            p.click()
            pyperclip.copy("""Prezado(a),

Agradecemos o envio da avaliação de eficácia. Porém só conseguiremos fazer a inclusão no sistema Metadados se a solicitação estiver conforme a IT DRH 0109.006 Metodologia De Avaliação De Eficácia disponível na Intranet.

Atenciosamente,
Treinamento e Desenvolvimento
""")
            p.hotkey('ctrl', 'v')
            self.reprovar()

#Aprovação
    def aprovar(self):
        p.confirm(text='Solicitação finalizada?', title='Continuar', buttons=['OK'])
        p.click(1000,0)
        p.press('end')
        p.click(757,572) #BOTÃO APROVA
        sleep(5)
        p.hotkey('ctrl','w')
        sleep(1)
        p.press('tab')
        sleep(1)

#Reprovação
    def reprovar(self):
        p.confirm(text='Solicitação finalizada?', title='Continuar', buttons=['OK'])
        sleep(1)
        p.click(843,579) #BOTÃO REPROVA
        sleep(3)
        p.hotkey('ctrl','w')
        sleep(5)
        p.press('tab')
        sleep(1)
