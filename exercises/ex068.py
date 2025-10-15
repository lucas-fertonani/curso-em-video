#ex068
#Faça um programa que jogue par ou ímpar com o computador.O jogo será interrompido quando o jogador Perder.
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
import random
count = 0
list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
jogada_computador = random.choice(list)
while True:
    count += 1
    n = int(input('Diga um valor: '))
    PI = input('Par ou Ímpar? [P/I]: ').upper()
    somacao = n+jogada_computador
    if somacao % 2 == 0:
        print(f'Voce jogou {n} e o computador jogou {jogada_computador}. Total de {somacao} DEU PAR')
        print('Voce Ganhou!')
        print(f'Voce venceu {count} vezes')
    elif somacao % 2 != 0:
        print(f'Voce jogou {n} e o computador jogou {jogada_computador}. Total de {somacao} DEU IMPAR')
        print('Você Perdeu!')
        print(f'Voce ganhou {count-1} vezes')
        break
    elif somacao % 3 != 0:
        print(f'Voce jogou {n} e o computador jogou {jogada_computador}. Total de {somacao} DEU PAR')
        print('Você Perdeu!')
        print(f'Voce ganhou {count+1} vezes')
        break
    elif somacao % 3 == 0:
        print(f'Voce jogou {n} e o computador jogou {jogada_computador}. Total de {somacao} DEU IMPAR')
        print(f'Voce Ganhou!')
        print(f'Voce ganhou {count+1} vezes!')