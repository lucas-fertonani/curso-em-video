#ex089
#Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.No final,mostre um boletim contendo a média de cada um e
#permita que o usuário possa mostrar as notas de cada aluno individualmente.


#CODIGO DO GUANABARA
ficha = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    resp = str(input('Voce quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*30)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    continuar = int(input('Voce quer mostrar nota de qual aluno? (999 interrompe): '))
    if continuar <= len(ficha) -1:
        print(f'As notas de {ficha[continuar][0]} sao: {ficha[continuar][1]}')
    elif continuar == 999:
        break
print('FINALIZANDO...')
print('<<<VOLTE SEMPRE>>>')

    





















#CODIGO QUE EU FIZ
# nome_notas = []
# nome_notas_lista_composta = []
# while True:
#     nome_notas.append(str(input('Nome: ')))
#     nome_notas.append(float(input('Nota 1: ')))
#     nome_notas.append(float(input('Nota 2: ')))
#     media = (nome_notas+nome_notas) / 2 
#     nome_notas_lista_composta.append(nome_notas)
#     continuar = input('Voce quer continuar? [Y/N]: ').upper()
#     if continuar != 'Y':
#         break
# print('-='*30)
# for pos in range(0,len(nome_notas_lista_composta)):
