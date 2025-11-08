#Aula 020
#Funções
#Funções é rotina e uma alguma coisa que você faz constantemente por exemplo tabela:
#mostrartabela()
#       |       |
#       |       |
#       |       |
#       |       |

#No python a função se chama "def",def = definição de função
#Ou seja função e criar e uma função personalizada que não existe no python.
#Exemplo:
print('----------------------------------')
print('        Cadastro de Saúde         ')
print('----------------------------------')
print('----------------------------------')
print('        Lista de Espera           ')
print('----------------------------------')
#inves de repetir a linha com traço 4 vezes poderemos usar as funções ou seja:
def rotinalinha():
    print('-------------------------------')
#agora com o rotinalinha() fica assim:
rotinalinha()
print('         Cadastro de Saúde         ')
rotinalinha()
rotinalinha()
print('         Lista de Espera           ')
rotinalinha()
#ele fica a mesma coisa do outro exemplo so que menos repetitivo


#A gente pode usar a estrategia do parametro do def como voce pode ver
#o bloco de cima que cadastro de saude é muito parecido com lista de espera mas so muda o que esta dentro desse bloco ou seja no meio entre as duas linhas.
#Então inves de:
print('----------------------------------')
print('        Cadastro de Saúde         ')
print('----------------------------------')
print('----------------------------------')
print('        Lista de Espera           ')
print('----------------------------------')
#Com o parametro ficaria assim:
def message(mensg):
    print('-----------------------------')
    print(mensg)
    print('-----------------------------')


message('ALISTAMENTO MILITAR')
message('TOP 10 COMIDAS DO BRASIL')
message('AS 7 MARAVILHAS DO MUNDO')


#Como empacotar dados com o sistema de Funções:
def count(* number):
    print(number)


count(14, 2, 4, 5, 7)
count(542, 1000)


#Definições com listas
def dobra(list):
    position = 0
    while position < len(list):
        list[position]*=2 
        position =+ 1
strings = ['BATATA','ARROZ','CARNE','FEIJÃO']
dobra(strings)


