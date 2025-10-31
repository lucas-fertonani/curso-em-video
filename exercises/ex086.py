#ex086
#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final,mostre a matriz na tela,com a formatação correta.


##CODIGO DO GUANABARA
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]',end=(' '))
    print()






















## CODIGO QUE EU FIZ
# lista_unica_1 = []
# lista_unica_2 = []
# lista_unica_3 = []
# for i in range(0,3):
#     linha_1_i = int(input(f'Digite um valor [0, {i}]: '))
#     lista_unica_1.append(linha_1_i)
# for d in range(0,3):
#     linha_2_d = int(input(f'Digite um valor [1, {d}]: '))
#     lista_unica_2.append(linha_2_d)
# for x in range(0,3):
#     linha_3_x = int(input(f'Digite um valor [2, {x}]: '))
#     lista_unica_3.append(linha_3_x)
# print(lista_unica_1)
# print(lista_unica_2)
# print(lista_unica_3)