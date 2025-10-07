#for c in range(0,10):
#    print(c)
#print('Fim')

#c = 1
#while c != 10:
#    print(c)
#    c = c + 1
#print('fim')

#for c in range(1,5):
#    n = int(input('Digite um valor: '))
#print('Fim')

#while n != 0:
#    n = int(input('Digite um valor: '))
#print('Fim')

#r = 'S'
#while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar? [S/N] ')).upper()
#print('Fim')
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Voce digitou {par} numeros pares')
print(f'Voce digitou {impar} numeros impares')
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares')
print(f'Voce digitou {impar} numeros impares')
print('Fim')