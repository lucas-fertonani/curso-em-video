#ex055
#Faça um programa que leia o peso de cinco pessoas.No final,mostre qual foi o maior e o menor peso lidos.

peso_maior = 0
peso_menor = 9999
for idx in range(0,5):
    peso_atual = float(input('Digite seu peso: '))
    if peso_atual > peso_maior:
        peso_maior = peso_atual
    if peso_atual < peso_menor:
        peso_menor = peso_atual
print(f'O maior peso é {peso_maior}')
print(f'O menor peso {peso_menor}')

