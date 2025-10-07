#ex017
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjente de um triangulo,retangulo,calcule
#e mostre o comprimento da hipotenusa

import math
co = int(input('qual é o comprimento do cateto oposto'))
ca = int(input('qual é o comprimento do cateto adjacente'))
formulahipotenusa = co**2 + ca**2
formulahipotenusa1 = math.sqrt(formulahipotenusa)
print('O comprimento do cateto da hipotenusa é de {}'.format(formulahipotenusa1))