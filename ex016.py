#Desafio 016
#Crie um programa que leia um numero Real qualquer pelo teclado e mostre sua porção inteira
import math
num = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(num,math.trunc(num)))