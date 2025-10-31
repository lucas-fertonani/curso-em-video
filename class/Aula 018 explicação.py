#Aula 018
#Variaveis compostas -> listas (parte 2)

#pra criar uma lista posso usar duas maneiras:
lista = list()
lista = []
#Pra salvar alguma coisa dentro da lista posso usar:
lista.append('Maria')
#Se eu utilizar outro append por exemplo ficaria:
lista.append('Maria')
lista.append(125)
#Ele vai criar o 0 e 1 indice 0 = Maria,1= Maria

#Posso mandar ele dar print no elemento 0 como:
lista.append('Maria')
lista.append(125)
print(lista[0]) #Codigo de saida -> Maria

#Vou declarar uma nova estrutura:
pessoas = []
#Inves de dar o append num valor vou dar append na estrutura:
pessoas.append(lista[:])
#entao so nao vai ter Maria ou 125 vai ter os dois maria e 125 vai ter duas listas fundidas entao ficaria a
#lista pessoa junto com a lista de Maria e 125 entao:
print(pessoas)
#Vai ter o elemento 0 que a lista que a gente colocou dentro de pessoas e o elemento 1 e vou colocar outra pessoa
#exemplo 
#elemento 0:'Maria',125
#elemento 1:vou adicionar 'Lucas',14
#elemento 2: 'Gabriel',52

#Como declarar todo essa estrutura de uma vez só:
pessoas = [['Maria',125],['Lucas',14],['Gabriel',52]]
#Indices
#1 indice = 'Maria',125
#2 indice = 'Lucas',14
#3 indice = 'Gabriel',52

#Um outro exemplo:
print(pessoas[0][0]) #-> Maria
#com essa print vou selecionar a lista pessoas e selecionar o elemento/indice 0
print(pessoas[1][1]) #-> 14
#com esse print vou selecionar o indice 1 e selecionar o elemento 1 que é o 19
print(pessoas[2][0]) #-> Gabriel
#com esse print vou selecionar o indice 2 e selecionar o elemento 0 que é o Gabriel
print(pessoas[1]) #-> Lucas,14
#com esse print vou selecionar o indice 1 inteiro que é Lucas,14