#ex025
#Crie um programa que leia um nome de uma pessoa e diga se ela tem 'Silva' no nome.
nome_completo = input('Digite seu nome completo: ')
nome_completo_min = nome_completo
tem_silva = 'silva' in nome_completo_min

print(f'Seu nome contem silva? vai aparecer quantos silva tem no nome ou seja {tem_silva}')