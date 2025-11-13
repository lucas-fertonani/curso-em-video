#ex101
#Crie um programa que tenha uma função chamada voto() que vai receber um parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
#pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
import time


print('-'*40)

def eleicao(ano_nascimento):
    tempo_atual = time.localtime()
    ano = tempo_atual.tm_year
    pessoa_anos = ano - ano_nascimento
    if pessoa_anos < 18:
       return print(f'Com {pessoa_anos} anos: NÃO VOTA!.')
    elif pessoa_anos > 17 and pessoa_anos < 70:
        return print(f'Com {pessoa_anos} anos: VOTO OBRIGATÓRIO.')
    else:
        return print(f'Com {pessoa_anos} anos: VOTO OPCIONAL')

ano_nascimento_1 = int(input('Em que ano você nasceu: '))
eleicao(ano_nascimento_1)
