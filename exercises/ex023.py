#ex023
#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos seperados
#ex:Digite um numero: 1834
#unidade:4,dezena:3,centena:8,milhar:1

import math
numero = input('Digite um número de 1000 a 9999: ')
print('Sua milhar é de {}!'.format(numero[0]))
print('Sua centena é de {}!'.format(numero[1]))
print('Sua dezena é de {}!'.format(numero[2]))
print('Sua unidade é de {}!'.format(numero[3]))
