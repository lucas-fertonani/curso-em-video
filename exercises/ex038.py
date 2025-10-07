#ex038
#Escreva um programa que leia dois numeros inteiros e compare-os,mostrando uma tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#-Nao existe valor maior os dois sao iguais
num_1 = int(input('Digite um numero: '))
num_2 = int(input('Digite o segundo numero: '))
if num_1 == num_2:
    print('Nao existe valor maior os dois sao iguais')
elif num_1 > num_2:
    print(f'O numero {num_1} é maior do que {num_2}!')
elif num_2 > num_1:
    print(f'o numero {num_2} é maior do que {num_1}!')