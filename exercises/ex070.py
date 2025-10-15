#ex070
#Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário vai
#continuar.No final,mostre:
#A) Qual é o total gasto na compra
#B) Quantos produtos custam mais de R$1000
#C) Qual é o nome do produto mais barato
count = 0
barato = ''
import pdb
menor_produto = 0
result_preco = []
produto_1000 = 0
while True:
    count =+ 1
    nome_produto = input('Nome do produto: ')
    preco = float(input('Preço: '))
    print('Compra registrada com sucesso!')
    continuar = input('Quer continuar [Y/N]: ').upper()
    result_preco.append(preco)
    if preco >= 1000:
        produto_1000 += 1
        menor_produto.append(nome_produto)
    if count == 1:
        menor_produto = preco
        barato = nome_produto
    else:
        if preco < menor:
            menor_produto = preco
            barato = produto
    if continuar != 'Y':
        break
print(f'Seu total gasto foi {sum(result_preco)}R$')
print(f'Tem {produto_1000} produtos que custam 1000R$')
print(f'O item mais barato registrado na sua compra eh uma/um {barato} de {menor_produto}')