#ex054
#Crie um programa que leia o ano de nascimento de sete pessoas.No final,mostre quantas atingiram a maioridade e quantas
#ja sao de menores

from datetime import date
idade_atual = date(2025,10,2)
for idx in range(0,7):
    nasc = int(input('Digite seu ano de nascimento: '))
    if nasc > idade_atual:
        idade_atual = nasc
    if nasc < idade_atual:
        idade_atual = nasc - nasc
print(f'{idade_atual} sao menores de 18')
print(f'{idade_atual} sao maiores de 18')


            
            
        



