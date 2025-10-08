#ex063
#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de
#Fibonacci.
#ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
sequencia = []
quantity = int(input("Digite a quantidade de fibonacci desejada: "))
count = 0

while True:
    if quantity<=count:
        break

    count += 1

    if count == 0:
        sequencia.append(0)

    elif count == 1:
        sequencia.append(1)

    else:
        sequencia.append(sequencia[len(sequencia)-2]+sequencia[len(sequencia)-1])
    

print(sequencia)