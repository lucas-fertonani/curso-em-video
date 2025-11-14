#ex107
#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importa esse módulo e use algumas dessas funções.
import utils.moeda as moeda
n = float(input('Digite o preço: '))
print(f'Aumentando seu dinheiro em 25%, temos {moeda.aumentar(n , 25)}R$')
print(f'Diminuindo seu dinheiro em 32%, temos {moeda.diminuir(n, 32)}R$')
print(f'Dobrando seu dinheiro fica {moeda.dobro(n)}R$')
print(f'Deixando na metade seu dinheiro fica {moeda.metade(n)}R$')