#Aula 017 prática
#Variaveis Compostas(listas)

#Lista sao mutaveis
num = [1,3,5,7,4,2,4]
num[3] = 5
num.append(8)
print(num)

#organizar os numeros
num = [5,3,6,8,3,4]
num.sort()
print(num)

#Organizar os numeros inversamente
num = [5,3,6,8,3,4]
num.sort(reverse=True)
print(num)

#Pra saber quantos elementos tem em uma lista
num = [3,4,2,5,3]
print(len(num))

#Pra adicionar elementos
num = [2,4,2,4,5]
num.insert(2,9)
print(num)

#Pra remover elementos
list_salgado = ['Batata Frita','Coxinha','Ravioli','Pizza','Macarrão']
list_salgado.pop(2,)
print(list_salgado) #-> eliminar o ultimo elemento da lista

list_salgado1 = ['Milho','Mandioca','Salgadinho','Carne Louca']
list_salgado1.remove('Milho')

list_salgado2 = ['Milho','Mandioca','Salgadinho','Carne Louca']
if 'Milho' in list_salgado2:
    list_salgado2.remove('Milho')
else:
    print('Não existe o Arroz')

#utilizando o append junto com o for
valores_atualizado = []
valores_atualizado.append(2)
valores_atualizado.append(3)
valores_atualizado.append(4)
for v in valores_atualizado:
    print(f'{v}...',end=(' '))

#Usando enumerate na lista
valores_atualizado = []
valores_atualizado.append(2)
valores_atualizado.append(3)
valores_atualizado.append(4)

for c, v in enumerate(valores_atualizado):
    print(f'Na posição {c} encontrei o valor {v}...')

#ler valores pelo teclado na lista
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
for c,v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}')

#pecualiaridade do python nas listas:
a = [5,3,12,4,6,7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')