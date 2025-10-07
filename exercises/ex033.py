#ex033
#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))
num_3 = float(input('Digite o terceiro número: '))

if num_1 > num_2 and num_1 > num_3:
    print(f'{num_1} é o maior')

if num_1 < num_2 and num_1 < num_3:
    print(f'{num_1} é o menor')

if num_2 > num_1 and num_2 > num_3:
    print(f'{num_2} é o maior')

if num_2 < num_1 and num_2 < num_3:
    print(f'{num_2} é o menor')

if num_3 > num_1 and num_3 > num_2:
    print(f'{num_3} é o maior')

if num_3 < num_1 and num_3 < num_2:
    print(f'{num_3} é o menor')





## and tudo precisa ser verdadeiro














