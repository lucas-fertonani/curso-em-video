#ex100
#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().A primeira função vai sortear 5 números e vai coloca-lós
#dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
numeros = []
for i in range(5):
    number = randint(0,50)
    numeros.append(number)


def sorteia():
    print(f'Sorteado os valores da lista {numeros} valores')
def somaPar():
    s = 0
    for pos,num in enumerate(numeros):
        if num % 2 == 0:
            s = s + num
    print(f'Os numeros sorteados dos {numeros} deu {s}')

sorteia()
somaPar()

