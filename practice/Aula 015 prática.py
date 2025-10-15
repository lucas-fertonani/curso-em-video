#Aula 015 prática

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
print(f'A soma desses numeros é {s}')