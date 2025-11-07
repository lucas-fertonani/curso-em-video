#ex095
#Aprimorie o desafio 093 para que ela funcione com vários jogadores,incluindo um sistema de visualização de detalhes
#do aproveitamento de cada jogador.


#APAGUEI MEU CODIGO SEM QUERER LEO SE VOCE VER ISSO NO GIT HUB :(

#CODIGO DO GUANABARA
time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Voce quer continuar [S/N]: '))
        if resp in 'Nn':
            break
        print('Erro! Responda com apenas S ou N')
    if resp == 'N':
        break
print('-='*40)
for i,j in enumerate(time):
    print((f'{k:>4}',end=(''))
    for d in v.values():
        print(f'{str(d):<15}',end=(''))
while True:
    busca = int(input('Mostrar dados de qual jogador (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro nao existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'no jogo {i+1} fez {g} gols')
print('<<<VOLTE SEMPRE>>>')