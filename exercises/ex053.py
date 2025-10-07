#ex053
#Crie um programa que leia uma frase e diga se ela e um palindromo.Desconsiderando os espacos

frase = str(input('Digite a sua frase: '))
frase_invertida = frase[::-1]
if frase_invertida == frase:
    print('E um palindromo')
elif frase_invertida != frase:
    print('Nao e um palindromo')