#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.No final mostre:
#A)Quantas vezes apareceu o valor 9
#B)Em que posição foi digitado o primeiro valor 3
#C)Quais foram os numeros pares.

n = (int(input('Digite um valor: '))),(int(input('Digite um valor: '))),(int(input('Digite um valor: '))),(int(input('Digite um valor: ')))
print(f'Voce digitou os valores: {n}')
print(f'O 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O 3 apareceu na {n.index(3)+1} posição')
else:
    print('O tres nao esta em nenhuma posição')
print('Os valores pares digitados foram: ')
for num in n:
    if n % 2 == 0:
        print(n)






































#cont = 0
#cont += 1
#n_pergunta = 0
#tupla_memoria = []
#n_par = 0
#tres_nao_digitado = 0
#n_nao_par = 0
#while cont < 5:
#    cont += 1
#    n_pergunta = int(input('Digite Quatro valores: '))
#    tupla_memoria.append(n_pergunta)
#    if n_pergunta % 2 == 0:
#        print(f'O numero {n_pergunta} {n_par}')
#    if n_pergunta % 3 == 0:
#        print(f'O numero {n_pergunta} Nao e par')
#print(tupla_memoria.count(9))
#print(tupla_memoria.index(3))
#print(f'O numero {n_pergunta} {n_nao_par}')
#print(f'O numero {n_pergunta} {n_par}')
