#ex057
#Faça um programa que leia o sexo de uma pessoa mas so aceite os valores 'M' ou 'F'.Caso esteje errado,peça a digitação
#novamente ate ter um valor correto.
genero_perguntado = ''
while genero_perguntado not in ['M','F']:
    user_input = input('Digite seu genero: ')
    genero_perguntado = user_input.upper().strip()


print('Sucesso!')    

#r = 'S'
#while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar? [S/N] ')).upper()
#print('Fim')