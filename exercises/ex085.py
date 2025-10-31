#ex085
#Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista única que mantenha separados valores pares e ímpares.No final,
#mostre os valores pares e ímpares em ordem crescente
n_impar = []
n_par = []
n = []
for c in range(0,7):
    n.append(int(input(f'Digite o {c+1}o. valor: ')))
    for i,v in enumerate(n):
        if v % 2 == 0:
            n_par.append(v)
        else:
            n_impar.append(v)
print(f'A lista completa > {n} ')
print(f'Os numeros pares são: {sorted(set(n_par))}')
print(f'Os numeros impares são: {sorted(set(n_impar))}')