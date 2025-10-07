#ex027
#Faca um programa que leia um nome completo de uma pessoa,mostrando em seguida o primeiro e ultimo nome
#separadamente


## Todos list: underline quando for espaco nas variaveis.

nome_completo = input('Digite seu nome completo: ')
nome_completo_separado = nome_completo.split(" ")


# O split separa a string em um lista, o primeiro argumento da funcao split, eh o separador


# variavel para

primeiro_nome = nome_completo_separado[0]
ultimo_nome = nome_completo_separado[-1]
print(f'O seu primeiro nome eh {primeiro_nome}!')
print(f'O seu ultimo nome eh {ultimo_nome}!')

# FOCA NISSO
## TIPOS DE DADO string, int, float, bool, list, dictionary