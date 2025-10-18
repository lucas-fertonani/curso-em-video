#ex078
#Faça um programa que leia 5 valores numéricos em uma lista
#No final mostre qual foi o maior e o menor valor digitado e a suas respectivas posições
memoria = []
n_menor = 0
n_maior = 0
for c in range(0,5):
    memoria.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        n_maior = n_menor = memoria[c]
    else:
        if memoria[c] > n_maior:
            n_maior = memoria[c]
        if memoria[c] < n_menor:
            n_menor = memoria[c]
print(f'Voce digitou os valores: {memoria}')
for i,v in enumerate(memoria):
    if v == n_maior:
        print(f'O maior número sera {n_maior} e ele está na posição {i}...')
    if v == n_menor:
        print(f'O menor número será {n_menor}, e ele esta na posição {i}...')