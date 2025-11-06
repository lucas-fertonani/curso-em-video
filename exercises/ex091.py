#ex091
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
from time import sleep
import random

dado = [1,2,3,4,5,6]

qtd_jogadores = int(input('Quantidade de jogadores: '))

jogadores = []

for idx in range(1,qtd_jogadores+1):
    jogador = {}
    dado_aleatorio = random.choice(dado)
    jogador["nome"] = f'Jogador{idx}'
    jogador["dado"] = dado_aleatorio
    jogadores.append(jogador)
    
jogadores_ordenados = sorted(jogadores, key=lambda d: d['dado'], reverse=True)

for idx, jogador in enumerate(jogadores_ordenados[:3]):
    print(f'{idx+1}- {jogador['nome']} - {jogador['dado']}')

