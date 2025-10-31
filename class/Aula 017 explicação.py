#Aula 017
#Variaveis compostas(listas)
Nas tuplas a gente usava: ()
agora na lista usaremos: []
entao por exemplo:
ps = ['ps1','ps2','ps3','ps4','ps5']
agora aquela regra que tinha na tupla que era imutavel,na lista nao vai contar ou seja ficaria assim:
ps = ['ps1','ps2','ps3','ps4','ps5']
ps[5] = 'ps vita'                  -> listas sao mutaveis
e de ps5 vai mudar pra ps vita

pra adicionar mais um elemento a lista usaremos esse comando:
ps.append('ps6')
e com isso ele adiciona no final da lista o que eu peço entao inves de:
ps = ['ps1','ps2','ps3','ps4','ps5']
vai ficar:
ps = ['ps1','ps2','ps3','ps4','ps5','ps6']
pra adicionar algum elemento por exemplo antes de ps1 usaremos o comando:
ps.insert(0,'ps vita atualizado')
---------------------------------------------------------------------------------
tem o comando de deletar que é o:
del ps[3] -> ele vai eliminar o ps2
outro comando de deletar um elemento:
ps.pop(3) -> ele vai eliminar o ps2 ,o pop em si sozinho ele serve pra eliminar o ultimo elemento
outro metodo de remover um elemento:
ps.remove('ps2') -> ele vai remover o ps2 da lista -> ele vai remover o elemnto e refazer o indice entao o indice que era:
['ps vita atualizado','ps1','ps2','ps3','ps4','ps5','ps6']
vai ficar:
['ps vita atualizado','ps1','ps3','ps4','ps5','ps6']
----------------------------------------------------------------------------------------------
como verficar se algum item esta na minha lista:
ps = ['ps1','ps2','ps3','ps4','ps5']
if 'ps7' in lanche:
    ps.remove('ps7') 
---------------------------------------------------------------------------------------------
Como criar listas atraves de range:
valores = list(range(4,11))
ele vai criar uma lista chamada valores com os elementos e com os indices ele vai colocar as posições de 0 ate 6
print(valores)  ->Codigo de saída: [4,5,6,7,8,9,10]

tem um metodo de organizar uma lista:
valores = [4,1,6,3,7,8,5,3]
valores.sort() -> ele vai ordenar todos os valores ou seja o codigo de saida vai ficar: [1,3,3,4,5,6,7,8]

se voce quer inverter a lista use este comando:
valores = [4,1,6,3,7,8,5,3]
valores.sort(reverse=True)
entao inves de ficar assim:
[1,3,3,4,5,6,7,8]
o codigo de saída vai ficar assim:
[8,7,6,5,4,3,3,1]

se voce quer saber quantos elementos tem em uma lista usaremos este comando:
valores = [4,1,6,3,7,8,5,3]
print(len(valores))
Codigo de saída = 8