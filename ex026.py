#ex026
#Faça um programa que leia uma frase do teclado e mostre
#quantas vezes aparece a letra 'a'
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece pela ultima vez

frase = input('Digite uma frase: ')

# Tranforme a frase em minuscula, para nao ter o proble de contabilizar os A
frase_minuscula = frase.lower()

contador = frase_minuscula.count('a')
primeira_posicao = frase_minuscula.find('a')
ultima_posicao = frase_minuscula.rfind('a')

print(f'A letra a aparece {contador} vezes')
print(f'A letra a começa na posição {primeira_posicao} ')
print(f'A letra a na ultima posição é {ultima_posicao}')