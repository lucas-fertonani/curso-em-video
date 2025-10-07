#desafio 004
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo de primitivo e todas as informações possiveís sobre ele

n = (input('Digite algo '))
print('o tipo primitivo desse valor é {}'.format(type(n)))
print('eh numero?',n.isnumeric())
print('Está em minúscula',n.islower())
print('Esta em maiúsculas?',n.isupper())
print('só  tem espaço?',n.isspace())
print('E numero decimal?',n.isdecimal())
print('Está em alfanumerico? ',n.isalnum())
print('está capitalizada? ',n.istitle())