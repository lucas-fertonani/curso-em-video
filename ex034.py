#ex034
#Escreva um programa que pergunte o salario de um funcionario e calcule seu valor do seu aumento

salario = float(input('Digite o seu salario: '))
if salario > 1250.0:
    salario_1250 = (salario*10)/100
    print(f'Seu aumento de salario será de {salario_1250} R$')

if salario <= 1250.0:
    salario_menos_1250 = (salario*15)/100
    print(f'Seu aumento de salario será de {salario_menos_1250} R$')