#ex088
#Faça um programa que ajude o jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
#para cada jogo,cadastrando tudo em uma lista composta

##CODIGO GUANABARA
from random import randint
lista = []
jogos = []

print('-'*30)
print(f'{'MEGA SENA':>20}')
print('-'*30)
quant = int(input('Quantos jogos voce quer que eu sorteie?: '))
tot = 1
while tot <= quant:
    count = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    print(jogos) 
print(f'Sorteando a quantidade de {quant} jogos...')
print(f'Jogo {count}: {jogos}')






#codigo que eu fiz
# import random
# lista_60 = list(range(0,61))
# jogada = random.choices(lista_60,k=6)
# jogo = int(input('Quantos Jogos voce quer que eu sorteie?: '))
# for i in (jogo):
#     if i == jogo:
#         print(i*sorted(jogada))
