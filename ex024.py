#ex024
#Crie um programa que leia um nome de uma cidade e diga se ela começa ou nao com o nome 'Santo'

cidade = input('Digite uma cidade: ')

# Essa variavel retorna 0 ou 1

cidade_minuscula = cidade.lower()
comeca_com_santo = cidade_minuscula.startswith("santos")

print(f'Caso sua cidade começe com "Santo" vou exibir 1, caso não começe vou exibir 0: {comeca_com_santo}')
