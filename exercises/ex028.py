#ex028
#Escreve um programa que faça um computador pensar em um numero inteiro entre 0 a 5 e peça pra usuario tentar
#descobrir qual foi o numero escolhido pelo o computador .
# o programa deverá escrever na tela se o usuario venceu ou nao

import random
jogada_do_usuario = int(input('Digite um numero de 0 a 5: '))
num = 1,2,3,4,5
jogada_do_computador = random.choice(num)

if jogada_do_usuario == jogada_do_computador:
    print('Parabens você ganhou!')
else:
    print('Você perdeu!')

print(f'U {jogada_do_usuario}')
print(f'C {jogada_do_computador}')