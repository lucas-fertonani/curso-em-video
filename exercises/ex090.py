#ex090
#Faça um programa que leia o nome e média de um aluno.Guardando também a situação em um dicionário.No final mostre
#o conteúdo da estrutura na tela

pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
if pessoa['Nome'] == '0':
    break
pessoa['Media'] = float(input('Média: '))
if pessoa['Media'] >= 7.0:
    print('Sua situação e igual a aprovado')
else:
    print('Sua situação e igual a reprovado')
