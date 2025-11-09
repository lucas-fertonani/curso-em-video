#ex096
#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
def area(largura,comprimento):
    area = largura * comprimento
    print(f'Seu terreno {area} metros quadrados')



c = float(input('Comprimento: '))
l = float(input('Largura: '))

area(l, c)