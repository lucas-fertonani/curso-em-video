#ex093
#Crie um programa que gerencie o aproveitamento de um jogador de futebol.O programa vai ler o nome do jogador e quantas 
#partidas ele jogou.Depois vai ler a quantidade de gols feitos em cada partida.No final,tudo isso será guardado em um
#dicionário,incluido o total de gols feitos durante o campeonato.

quantidade_de_gols = 0
resultado = {}
resultado["nome"] = str(input('Nome do jogador: '))
resultado["gols"] = []

qnt_de_partidas = int(input(f'Quantas partidas {resultado['nome']} jogou?: '))

for c in range(1,qnt_de_partidas+1):
    gols = int(input(f'Quantos gols na partida {c}: '))
    resultado["gols"].append(gols)

print('-='*30)
print(resultado)
print('-='*30)

resultado["total"] = sum(resultado["gols"]) 

print(f'O campo tem o valor {resultado["nome"]}')
print(f'O campo de gols tem o valor {resultado["gols"]}')
print(f'total {resultado["total"]}')




print('-='*30)
print(f'O jogador {resultado["nome"]} jogou {qnt_de_partidas} partidas.')
for pos, num in enumerate(resultado["gols"]):
    print(f'    => Na partida {pos+1}, fez {num} gols')
print(f'Foi um total de {resultado["total"]} gols')


# resultado = {
#     "nome": "Exemplo",
#     "qnt_partidas": 15,
#     "gols": [1,2,5,3]
# }