#ex087
#Aprimorie o desafio anterior,mostrando no final:
#A-) A soma de todos os valores pares digitados.
#B-) A soma de todos os valores da terceira coluna.
#C-) O maior valor da segunda linha.


##CODIGO QUE O GUANABARA
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_1 = 0
soma_2 = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]',end=(' '))
    if matriz[l][c] % 2 == 0:
        soma_1 += matriz[l][c]
    print()
print(f'A soma de todos os valores digitados eh {sum(matriz[l][c])}')
for l in range(0, 3):
    soma_2 += matriz[l][2]
print(f'A soma de todos valores da terceira linha eh {soma_2}')
for l in range(0, 3):
    if matriz[l][2] > maior:
        maior = matriz[l][2]
print(f'O maior valor da segunda linha eh {maior}')
    












#CODIGO QUE EU FIZ:
#  matriz = [[0,0,0],[0,0,0],[0,0,0]]
# maior = 0
# par = []

# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-='*30)
# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[ {matriz[l][c]} ]',end=(' '))
#     print()
#     for v,i in enumerate(matriz):
#         if v % 2 == 0:
#             par.append(i)
#     for n in (matriz):
#         n.append(sum(matriz[c]))
#     if matriz[c][2] > maior:
#         maior = matriz[c][2]
# print(i)
# print(n)
# print(maior)