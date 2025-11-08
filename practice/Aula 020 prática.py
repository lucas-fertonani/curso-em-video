#Aula 020 prática
#Funções

#Definição com ints
def multiplicacao(x,y):
    print(f'X = {x}, Y = {y}')
    print('-'*30)
    z = x * y
    print(f'A multiplicação de {x} e {y} e igual a {z}')


multiplicacao(45,2)
multiplicacao(872,4)
multiplicacao(y=36,x=9)










#Definação com empacotamentos
from time import sleep
def linhas():
    print('------------------------------')


def ler(texto):
    print('<<< CARREGANDO INFORMAÇÕES >>>')
    sleep(1.0)
    print()
    ler_texto = len(texto)
    print('<<< SUAS INFORMAÇÕES FORAM CARREGADAS >>>')
    print()
    print(f'SEU TEXTO {texto} TEM {ler_texto} caracteres')

linhas()
ler('PRAIA')
linhas()
ler('PNEUMOULTRAMICROSCOPICOSILICOLVUCANOCONIOTICO')
linhas()
ler('EU TE AMO')
linhas()


#Definições com listas
def dobra(list):
    position = 0
    while position < len(list):
        list[position] *= 2 
        position += 1


strings = [0,1,2,3,4,5,6,7]
dobra(strings)
 
