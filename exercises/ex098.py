#ex098
#Faça um programa que tenha uma função chamada contador(),que receba três parâmetros:inicio,fim e passo e realize a contagem.

#Seu programa tem que realizar três contagens através da função criada:
#A-) De 1 até 10 ,de 1 em 1.
#B-) De 10 ate 0, de 2 em 2.
#C-)Uma contagem personalizada.
from time import sleep
def contador(numero):
    print('=-'*30)
    print('Contagem de 1 até 10 de 1 em 1')
    for idx in range(1,11):
        print(idx,end=(' '))
    print('FIM!')
    print('-='*30)
    print('Contagem de 10 até 0 de 2 em 2')
    for num in range(10,-2,-2):
        print(num,end=(' '))
    print()
    print('-='*30)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for positivo in range(i,f+p,p):
        print(positivo,end=(' '))
    for personalizar in range(i,f,-p):
        print(f'{personalizar}',end=(' '))
    print('Fim!')

c = contador

contador(c)

    