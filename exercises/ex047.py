#ex047
#Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50

#for c in range(0,52,2):
#   print(c,end=(' '))
#print('Numeros pares de 0 ate 50')

for c in range(1,51):
    if c % 2 == 0:
        print(c,end=(' '))