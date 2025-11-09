#ex097
#Faça um programa que tenha uma função chamada escreva().Que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#Ex:
#escreva('Olá mundo!')

#Saída:
#-------------
#   'Olá mundo!'
#-------------

def escreva(texto):
    print('--'+'-'*len(texto)+'--')
    print('/ ' + texto + ' \\')
    print('--'+'-'*len(texto)+'--')

t = input('Texto: ')
escreva(t)
