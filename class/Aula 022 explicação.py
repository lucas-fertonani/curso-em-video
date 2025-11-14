#Aula 022
#Módulos e Pacotes

#Modularização -> é um ato de construir módulos, o foco da modularização é dividir um programa grande e aumentar a legibilidade do programa.

#por exemplo nos modulos:
def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

#O código ficou grande entao eu divido ela em um arquivo por exemplo: multplicação.pg e guardo:
def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

#E o codigo principal fica assim:
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

#Isso que eu fiz se chama de MÓDULO


#Vantangens de usar MÓDULOS:
#-Organização do código.
#-Facilidade na manutenção.
#-Ocultação de código detalhado.
#-Reutilização em outros projetos.




#PACOTES

