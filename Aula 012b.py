import random
print('Jogo do PEDRA PAPEL E TESOURA')
lista = ['PEDRA,PAPEL,TESOURA']
jogada_do_usuario = str(input('Escolha PEDRA,PAPEL,TESOURA: '))
jogada_do_computador = random.choices(lista)
if jogada_do_usuario == jogada_do_usuario:
    print('Empate')
elif jogada_do_usuario == 'PEDRA' and jogada_do_computador == 'TESOURA':
    print('Voce ganhou!')
elif jogada_do_usuario == 'PAPEL' and jogada_do_computador == 'TESOURA':
    print('Voce ganhou!')
elif jogada_do_usuario == 'PAPEL' and jogada_do_computador == 'PEDRA':
    print('Você ganhou!')
elif jogada_do_usuario == 'TESOURA' and jogada_do_computador == 'PEDRA':
    print('Você perdeu!')
elif jogada_do_usuario == 'PEDRA' and jogada_do_computador == 'PAPEL':
    print('Voce perdeu!')
elif jogada_do_usuario == 'TESOURA' and jogada_do_computador == 'PAPEL':
    print('Voce ganhou!')
else:
    print('Jogada invalida')
