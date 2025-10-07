#ex 045
#Crie um programa que faça o computador jogar jokenpo com voce
import random
from xml.dom.pulldom import PROCESSING_INSTRUCTION

lista_jokenpo = ['PEDRA','PAPEL','TESOURA']
jogada_do_usuario = str(input('Escolha PEDRA PAPEL ou TESOURA: '))
jogada_do_computador = random.choice(lista_jokenpo)
if jogada_do_usuario == jogada_do_computador:
    print('EMPATE')
elif jogada_do_usuario == 'PEDRA' and jogada_do_computador == 'PAPEL':
    print('Você perdeu!')
elif jogada_do_usuario == 'PEDRA' and jogada_do_computador == 'TESOURA':
    print('Você ganhou!')
elif jogada_do_usuario == 'PAPEL' and jogada_do_computador == 'PEDRA':
    print('Você ganhou!')
elif jogada_do_usuario == 'PAPEL' and jogada_do_computador == 'TESOURA':
    print('Você perdeu!')
elif jogada_do_usuario == 'TESOURA' and jogada_do_computador == 'PEDRA':
    print('Você perdeu!')
elif jogada_do_usuario == 'TESOURA' and jogada_do_computador == 'PAPEL':
    print('Você ganhou!')
else:
    print('Jogada Invalida')

print(f'Jogada do usuario:{jogada_do_usuario}')
print(f'Jogada do computador:{jogada_do_computador}')
