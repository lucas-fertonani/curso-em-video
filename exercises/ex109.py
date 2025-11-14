#ex109
#Modifique as funções que foram criadas no desafio 107 para que eles aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
#formatado pela função moeda() desenvolvida no desafio 108.
import utils.moeda as moeda
n = 10
print(moeda.dobro(n, True))
print(moeda.metade(n, True))
print(moeda.aumentar(n,20, True))
print(moeda.diminuir(n,25, True))