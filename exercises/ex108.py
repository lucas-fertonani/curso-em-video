#ex108
#Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado. 
import utils.moeda as moeda

string = 'R$'
n = float(input('Digite o preço: '))
print(moeda.metade(n))
print(moeda.dobro(n))
print(moeda.aumentar(n,25))
print(moeda.diminuir(n,25))