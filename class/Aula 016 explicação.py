#Aula 016
#Variavéis compostas(Tuplas)

#Existem tres tipos de variavéis compostas:Tuplas,Listas e dicionario
#se eu quero adicionar um monte de coisa dentro de uma variavel só e possivel usando a tupla lista ou dicionario
#por exemplo
lanche = hamburger,suco,pizza,pudim
#no python sao organizados por quadrados ou seja: quadrado_1 -> hamburger,quadrado_2 -> suco,quadrado_3 -> pizza
#quadrado_4 -> pudim
#entao tipo fica assim: lanche_1 = hamburger,lanche_2 = suco,lanche_3 = pizza,lanche_4 = pudim
#Por exemplo em fatiamento:
print(lanche[2]) -> isso vai me mostrar somente a pizza
print(lanche[0:2]) -> isso vai me mostrar somente o hamburger e suco
print(lanche[1:]) -> isso vai me mostrar somente do suco até o final que é do suco até o pudim
print(lanche[-1]) -> isso vai me mostrar somente o ultimo elemento que é o pudim    

#Len
por exemplo o len ele mostra quantos elementos tem na variavel(tupla) entao fica:
len(lanche) -> codigo de saída = 4

#Estrutura de controle
por exemplo posso usar o for,while e while True, com as tuplas entao ficara assim:
for c in lanche:
    print(c) 
e quando ele passou de printar hamburger ele vai começar a printar o suco por que é um loop entao iria pro suco
depois pra pizza e depois pro pudim e depois ele vai comando abaixo do print e depois e so segue o resto do comando

#Conceito importante
lanche = hamburger,suco,pizza,pudim
por exemplo quero trocar um pudim pelo sorvete,Ai vem uma pequena limitação que é:"AS TUPLAS SAO IMUTAVEIS",no 
python e impossivel fazer essa mudança então nao da pra tirar o pudim