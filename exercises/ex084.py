#ex084
#Faça um programa que leia o nome e peso de varias pessoas,guardando tudo em uma lista,no final,mostre:
#A-) Quantas pessoas foram cadastradas.
#B-) Uma listagem com as pessoas mais pesadas
#C-) Uma listagem com as pessoas mais leves

#Codigo que o Guanabara
temp = []
princ = []
maior = 0
menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = men = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(princ[0])} pessoas')
print(f'O maior peso foi de {maior}KG ,Peso de ',end=(''))
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}',end=(' '))
print()
print(f'O menor peso foi de {menor}KG. Peso de',end=(''))
for idx in princ:
    if p[1] == menor:
        print(f'{p[0]}',end=(' '))





























##Codigo que eu fiz:
# nome_peso_lista_unica = []
# peso_maior = 0
# peso_menor = 0
# nome_peso_lista_composta = []
# while True:
#     nome_peso_lista_unica.append(str(input('Nome: ')))
#     nome_peso_lista_unica.append(float(input('Peso: ')))
#     nome_peso_lista_composta.append(nome_peso_lista_unica[:])
#     nome_peso_lista_unica.clear()
#     continuar = input('Você quer continuar? [Y/N]: ').upper()
#     if continuar != 'Y':
#         break
# print(f'Foram cadastradas {len(nome_peso_lista_composta[0])} pessoa\pessoas')
# for n in enumerate(nome_peso_lista_composta[1]):
#     if n > peso_maior:
#         peso_maior = n
#     if peso_menor > n:
#         peso_menor = n
# print(f'A pessoa mais pesada pesa {peso_maior}KG e o nome dela é {peso_maior[0]}')
# print(f'A pessoa mais leve pesa {peso_menor}KG e nome dela é {peso_menor[0]}')
