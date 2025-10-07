#ex022
#Crie um programa que leia um nome completo de um pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

nomecompleto = input('Digite seu nome completo: ')
print('Seu nome completo em letras maiusculas é {}!'.format(nomecompleto.upper()))
print('Seu nome completo em letras minusculas é {}!'.format(nomecompleto.lower()))
print('O seu nome completo tem {} letras!'.format(len(nomecompleto)))
primeironome = nomecompleto.split()
print('O seu primeiro nome tem {} letras!'.format(len(primeironome[0])))