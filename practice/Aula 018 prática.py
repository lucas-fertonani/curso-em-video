#Aula 018 prática:
#Variaveis compostas(Listas parte 2)

teste = []
teste.append('Lucas')
teste.append('14')
galera = []
galera.append(teste[:])
teste[0] = 'Matheus'             #<- codigo saída: [['Lucas',14], ['Matheus'], 17]
teste[1] = 17
galera.append(teste[:])
print(galera)

pessoal = [['João',19],['Ana', 33],['Joaquim',13],['Maria',45]]
print(pessoal)
print(pessoal[0])
print(pessoal[0][0])
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade')

pessoas = []
dado = []
total_menor = 0
total_maior = 0
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(pessoas)

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        total_maior =+ 1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor =+ 1
print(f'Temos {total_maior} maiores e {total_menor} de idades')