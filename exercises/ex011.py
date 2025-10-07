#ex011
#Faça um programa que leia a largura e a altura de uma parede em metros,calcule sua area e a quantidade
#de tinta nescessaria para pinta-la,sabendo que cada litro de tinta pinta uma area de 2m ao quadrado

largura = int(input('Digite quantos de largura em metros tem sua parede: '))
altura = int(input('Digite quantos de altura em metros tem sua parede: '))
area = largura*altura
print('A area da parede e de {} metros!'.format(area))
print('A quantidade de tinta nescessaria para pinta-la é de {} ml de tinta!'.format(area/2))