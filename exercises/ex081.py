#ex081
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso mostre:
#A)Quantos números foram digitados.
#B)A lista de valores ordenada de forma decrescente.
#C)Se o valor 5 foi digitado e está ou não na lista.

lista = []
for c in range(0,5):
    lista.append(int(input((f'Digite um valor na posição {c}: '))))
print(f'Foram digitados números: {len(lista)}')
print(f'Sua lista de valores de forma decrescente: {sorted(lista,reverse=True)}')
if 5 in lista:
    print('5 foi digitado na sua lista')
else:
    print('5 nao foi digitado na sua lista')










































#list1 = []
#while True:
#    num = int(input('Digite um valor: '))
#    continuar = input('Voce quer continuar:[Y/N]: ').upper()
#    list1.append(num)
#    if continuar != 'Y':
#        break
#print(f'Foram digitados {len(list1)} números/número')
#print(f'A ordem em decrescente dos números são: {sorted(list1,reverse=True)}')
#if 5 in list1:
#    print('O numero 5 foi digitado')
#else:
#    print('O numero 5 nao foi digitado')