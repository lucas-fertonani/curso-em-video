#desafio 036
#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.O programa
#vai perguntar o valor da casa o valor do salario do comprador e em quantos anos ele vai pagar

#Calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do salario ou entao o
#emprestimo sera negado.

print('Você não podera exceder de 30% do salario')
valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite o valor do seu salario: '))
tempo = float(input('Digite em quantos anos voce vai pagar a casa: '))
valor_mensal = valor_salario/tempo
emprestimo_negado = valor_salario*30/100
if valor_mensal > emprestimo_negado:
    print('Emprestimo negado!')
elif valor_mensal < emprestimo_negado:
    print('Emprestimo feito com sucesso!')



