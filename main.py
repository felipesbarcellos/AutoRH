from controle import Controle
import pyautogui
from time import sleep, time

#instanciando as classes
c1 = Controle()

#main
def main():
    while True:
        ti = time()
        limite = int(input('Quantas avaliações devem ser aprovadas? '))
        i = 0
        pyautogui.click(1000,0,1)
        while i < limite:
            tempo_inicial = time()
            c1.abre_solicitacao()
            c1.escreve_mensagem()
            i += 1
            tempo_final = time()
            print(f'Tempo na {i}ª solicitação: {tempo_final - tempo_inicial:.2f} segundos.')
                
        else:
            print('Concluído com Sucesso!')
        tf = time()
        print(f'Tempo total da execução: {(tf-ti)//60} minutos e {(tf-ti):.0f} segundos')

if __name__ == '__main__':
    main()
