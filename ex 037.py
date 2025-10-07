#037 desafio
#Escreva um programa que leia um numero inteiro qualquer peça para o usuario escolher qual
#sera a base da conversao: 1 para binario,2 para octal,3 para hexadecimal

num = int(input('Digite numero inteiro : '))
num_binario = int(input('Digite (1) se voce quer transformar em numero binario: '))
num_octal = int(input('Digite (2) se voce quer transformar em numero octal: '))
num_hexadecimal = int(input('Digite (3) se voce quer transformar em hexadecimal: '))

if num_binario == 1:
    print('Seu numero {} em binario vira: {}'.format(num, bin(num_binario)))
elif num_octal == 2:
    print('Seu numero {} em octal vira: {}'.format(num,oct(num_octal)))
elif num_hexadecimal == 3:
    print('Seu numero {} em hexadecimal vira: {}'.format(num,hex(num_hexadecimal)))