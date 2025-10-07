#ex044
#Elabore um programa que calcule o seu valor a ser pago por um produto considerando o seu preço normal
#e condição do pagamento:
#-A vista dinheiro/cheque 10% de desconto
#-A vista no cartao 5% de desconto
#em ate 2x no cartao preço normal
#3x ou mais no cartao: 20% de juros

produto_valor = float(input('Digite o preço do seu produto: '))
print('Digite [1] se voce deseja pagar a vista em cheque/dinheiro')
print('Digite [2] se voce deseja pagar a vista no cartao')
print('Digite [3] se voce deseja pagar em 2x no cartao')
print('Digite [4] se voce deseja pagar 3x ou mais no cartao')
opcao = int(input('Digite sua escolha: '))
opcao_4 = int(input('Se pagara pelo 4 metodo coloque em quantos vezes em cartao pagara: '))
vista_dinheiro_cheque = produto_valor-produto_valor*10/100
vista_cartao = produto_valor-produto_valor*5/100
mes2x_cartao = produto_valor
mes3x_ou_mais_no_cartao = produto_valor*0.20*opcao_4
if opcao == 1:
    print(f'Voce pagara {vista_dinheiro_cheque} R$ em seu produto')
elif opcao == 2:
    print(f'Voce pagara {vista_cartao} R$ em seu produto')
elif opcao == 3:
    print(f'Voce pagara {mes2x_cartao} R$ em seu produto')
elif opcao == 4:
    print(f'Voce pagara {mes3x_ou_mais_no_cartao} R$ no seu produto')
