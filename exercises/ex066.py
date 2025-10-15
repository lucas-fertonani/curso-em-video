#ex 066
#Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# 999,que a condição de parada.No final,mostre quantos números foram digitados e qual foi a soma deles(descosiderando
# a flag).
n = s = 0
count = 0
while True:
    count += 1
    n = int(input('Digite um número (Digite 999 para parar): '))
    if n == 999:
        break
    s = s + n
print(f'A soma dos {count-1} valores deu: {s}')