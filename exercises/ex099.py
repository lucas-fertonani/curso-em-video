#ex099
#Faça um programa que tenha uma função chamada maior(),que receba vários parâmetros com valores inteiros.

#Seu programa tem que analisar todos e dizer todos os valores e dizer qual é o maior.

from random import randint



def maior():
    n_maior = 0
    lista = []
    for i in range(5):
        numero = randint(0,100)
        lista.append(numero)
    print('-='*30)
    print('Analisando os valores passados...')
    print(lista,f'foram informados {len(lista)} valores ao todo')
    for pos,num in enumerate(lista):
        if num > n_maior:
            n_maior = num
    print(f'O maior valor informado foi {n_maior}')



    n_maior_1 = 0
    lista_1 = []
    for i in range(3):
        numero_1 = randint(0,100)
        lista_1.append(numero_1)
    print('-='*30)
    print('Analisando os valores passados...')
    print(lista_1,f'foram informados {len(lista_1)} valores ao todo')
    for pos,num in enumerate(lista_1):
        if num > n_maior_1:
            n_maior_1 = num
    print(f'O maior valor informado foi {n_maior_1}')



    n_maior_2 = 0
    lista_2 = []
    for i in range(2):
        numero_2 = randint(0,100)
        lista_2.append(numero_2)
    print('-='*30)
    print('Analisando os valores passados...')
    print(lista_2,f'foram informados {len(lista_2)} valores ao todo')
    for pos,num in enumerate(lista_2):
        if num > n_maior_2:
            n_maior_2 = num
    print(f'O maior valor informado foi {n_maior_2}')




    n_maior_3 = 0
    lista_3 = []
    for i in range(1):
        numero_3 = randint(0,100)
        lista_3.append(numero_3)
    print('-='*30)
    print('Analisando os valores passados...')
    print(lista_3,f'foram informados {len(lista_3)} valor ao todo')
    for pos,num in enumerate(lista_3):
        if num > n_maior_3:
            n_maior_3 = num
    print(f'O maior valor informado foi {n_maior_3}')



    n_maior_4 = 0
    lista_4 = []

    for i in range(0):
        numero_4 = randint(0,100)
        lista_4.append(numero_4)
    print('-='*30)
    print('Analisando os valores passados...')
    print(lista_4,f'foram informados {len(lista_4)} valores ao todo')
    for pos,num in enumerate(lista_4):
        if num > n_maior_4:
            n_maior = num
    print(f'O maior valor informado foi {n_maior_4}')



maior()