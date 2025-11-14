#Aula 022 prática
#Módulos e Pacotes
#Pacotes
#Pacotes são pastas que contém módulos então eu vou ter um pacote sobre o módulo e posso separar por assuntos por exemplo:

#So trata de cadastros
def cad_1():

def cad_2():

def cad_3():


#So trata de números decimais:
def floats_1():

def floats_2():

def floats_3():

#Ou seja dentro de pacotes eu tenho vários módulos separados por assunto
#pra importar esse pacote e so eu colocar:
import utilies
#ou se eu quero importar um determinado módulo:
from utilies import cadastros

#Como criar um pacote:
from utilies import numbers
num = int(input('Digite um valor:'))
fat = fatorial.utilies(num)
print(f'O fatorial de {num} é {fat}')