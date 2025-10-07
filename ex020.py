#ex020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos.
#faca um programa que leia o nome de quatro alunos e mostre a ordem sorteada

import random

list1 = ['lucas','enzo','miguel','pietro']
print('Quem vai apresentar primeiro eh {}!'.format(random.choice(list1)))