#ex080
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,já na posição
#correta da inserção(sem usar o sort()).
#No final mostre a lista ordenada na tela
cadastros = []
for n in range(0,5):
    num = int(input('Digite um valor: '))
    if n == 0:
        cadastros.append(n)
    elif n > cadastros[len(cadastros)-1]:            #<- pegar o ultimo elemento da lista
        cadastros.append(n)
    else:
        pos = 0
        while pos < len(cadastros):
            if n <= cadastros[pos]:
                cadastros.insert(pos,n)
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {cadastros}')

    