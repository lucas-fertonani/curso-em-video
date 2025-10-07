#ex065
#Crie um programa que leia varios numeros inteiros pelo teclado.No final da execução,mostre a media entre todos os valores
#e qual foi o menor e o maior valores lidos.O programa deve perguntar ao usuario se ele quer continuar a digitar valores

n_maior = 0
n_menor = 99999999999
result = []

while True:
    n = int(input('Digite um numero: '))
    if n > n_maior:
        n_maior = n

    if n < n_menor:
        n_menor = n
        
    result.append(n)
    nova_chance = input('Voce quer digitar novos numeros [Y/N]: ').upper()
    if nova_chance != "Y":
        break
print(n_maior,n_menor)
print(sum(result)/len(result))
    


        