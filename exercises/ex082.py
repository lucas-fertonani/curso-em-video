#ex082
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso,crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente
#Ao final,mostre o conteúdo das três listas geradas.
n = []
n_par = []
n_impar = []
while True:
    n.append(int(input('Digite um valor: ')))
    continuar = input('Voce quer continuar:[Y/N]: ').upper()
    if continuar != 'Y':
        break
for i,v in enumerate(n):
    if v % 2 == 0:
        n_par.append(v)
    else:
        n_impar.append(v)
print(f'A lista completa é: {n}')
print(f'Os numeros pares são:{n_impar}')
print(f'Os numeros pares são: {n_par}')



