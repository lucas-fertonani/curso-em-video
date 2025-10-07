#ex058
#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.Só que agora o jogador vai tentar
#adivinhar até acertar,mostrando no final quantos palpites foram necessarios para vencer.

import random
lista = [0,1,2,3,4,5,6,7,8,9,10]
jogada_do_computador = random.choices(lista)
adivinhar_computador = ''
count = 0
while adivinhar_computador != jogada_do_computador:
    adivinhar_computador = int(input('Digite um número: '))
    if adivinhar_computador > count:
        count = adivinhar_computador + 1
print(f'Você adivinhou o numero em {count-1} tentativas')













#Desafio 028
#import random
#jogada_do_usuario = int(input('Digite um numero de 0 a 5: '))
#num = 1,2,3,4,5
#jogada_do_computador = random.choice(num)
#
#if jogada_do_usuario == jogada_do_computador:
#    print('Parabens você ganhou!')
#else:
#    print('Você perdeu!')
#
#print(f'U {jogada_do_usuario}')
#print(f'C {jogada_do_computador}')