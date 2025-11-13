#ex103
#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome,gols):
    if nome == '' and gols == '':
        print('O jogador <desconhecido> fez 0 gols no campeonato')
    elif nome == '':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


# Teste 1: Deve retornar O jogador <desconhecido> fez 0 gols no campeonato
ficha('', '')

# Teste 2: Deve retornar O jogador <desconhecido> fez X gols no campeonato
ficha('',3)

# Teste 3: Deve retornar O jogador Felipe fez 7 gols no campeonato
ficha('Felipe',7)