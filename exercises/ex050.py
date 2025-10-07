#ex050
#Desenvolva um programa que leia seis numeros inteiros e mostre a soma deles apenas do que forem pares. se o valor digitado
#for impar desconsidere-o
soma = 0
for x in range (0,6):
    n = int(input('Digite algum valor: '))
    if n % 2 == 0:
        soma = soma + n
print(soma)


