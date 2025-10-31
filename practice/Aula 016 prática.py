#Aula 016 prática
#Variavéis compostas(tuplas)

#Criando a situação do lanche da explicação 016.py
lanche = ('Hambúrger','Suco','Pizza','Pudim')       <- Codigo de saída: ('Hamburger','Suco','Pizza','Pudim')
print(lanche)

lanche = ('Hambúrger','Suco','Pizza','Pudim')       <- Codigo de saída:'Suco'
print(lanche[1])

lanche = ('Hambúrger','Suco','Pizza','Pudim')       <- Codigo de saída:'Pizza'
print(lanche[-2])

lanche = ('Hambúrger','Suco','Pizza','Pudim')       <- Codigo de saída:('Suco','pizza')
print(lanche[1:3])

lanche = ('Hambúrger','Suco','Pizza','Pudim')       <- Codigo de saída:('Pizza','Pudim')
print(lanche[2:])

lanche = ('Hambúrger','Suco','Pizza','Pudim')       <- Codigo de saída:('Hamburger','Suco')
print(lanche[:2])

lanche = ('Hambúrger','Suco','Pizza','Pudim')       <- Codigo de saída:('Pizza','Pudim') 
print(lanche[-2:])

#Colocando em prática Conceito importante
#Tuplas sao imutáveis
lanche = ('Hambúrger','Suco','Pizza','Pudim')
lanche[1] = 'Refrigerante'       -> Erro
print(lanche[1])
#Vai dar erro de tupla

pra aparecer bonitinho sem aspas e parenteses colocamos assim:
lanche = ('Hambúrger','Suco','Pizza','Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba!')

pra contar os elementos de 1 a 4 é assim:
lanche = ('Hambúrger','Suco','Pizza','Pudim')
print(len(lanche))
print('Eu comi pra caramba!')

pra contar os elementos so pela a string e assim:
lanche = ('Hambúrger','Suco','Pizza','Pudim')
for cont in range(0,len(lanche)):
    print(lanche[cont])
print('Comi pra caramba')

lanche = ('Hambúrger','Suco','Pizza','Pudim')
for pos,comida in enumerate(lanche):                  <- Para mostrar a posição das comidas e a propria string da comida
    print(f'Eu comi a {comida} na posição {pos}')
-------------------------------------------------------------------------------------------------------------------------

lanche = ('Hambúrger','Suco','Pizza','Pudim')
print(sorted(lanche))       <- sorted = organizado
-> Codigo de saída = ['hambúrger','Pizza','Pudim','Suco']

---------------------------------------------------------------------------------------------------------------------
a = (0,5,8,10,4)
b = (20,7,11,14)
c = a + b -> ordem altera o fator se muda b + a ficaria = (14,11,7,20,4,10,8,5,0)
print(c)       -> Codigo de saida = (0,5,8,10,4,20,7,11,14)

a = (0,5,8,10,4)
b = (20,7,11,14)
c = b + a
print(c.count(5)) -> Codigo de saída = 1    -> Apareceu 1 por que aparece o 5 uma vez só

a = (0,5,8,10,4)
b = (20,7,11,14)
c = b + a
print(c.index(5)) -> Codigo de saída = 5     -> por que o 5 esta na posição 5


a = (0,5,8,10,4)
b = (20,7,4,14)
c = b + a
print(c.index(4,3)) Codigo de saída = 9 -> Por que somente vai mostrar a posição do ultimo 4
------------------------------------------------------------------------------------------------------------------
pessoa = ('Lucas',14,'M',51.2)
del(pessoa) -> del = delete
print(pessoa)    -> Codigo de saída: erro -> por que apagou a variavel


max = maior numero de uma tupla
min = menor numero de uma tupla