from time import time
from auto import Auto

a = Auto()

def main():
    while True:
        t_inicial = time()
        limite = int(input('Quantas avaliações devem ser aprovadas?  '))
        i = 0
        a.seleciona_primeira_solicitacao()
        while i < limite:
            tempo_inicial = time()
            a.abre_solicitacao()
            a.espera()
            a.copia_numero()
            a.baixa_pdf()
            a.abre_pdf()
            a.escreve_mensagem()
            i += 1
            tempo_final = time()
            print(f'Tempo na {i}ª solicitação: {tempo_final - tempo_inicial:.2f} segundos.')
        else:
            print('Concluído com sucesso!')
        t_final = time()
        print(f'Tempo total da execução: {(t_final-t_inicial)//60} minutos e {(tf-ti):.0f} segundos')


if __name__ == '__main__':
    main()
