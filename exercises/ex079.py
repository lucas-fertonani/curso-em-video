#Ex079
#Crie um programa onde o usuário possa digitar varios valores númericos e cadastre-os em uma lista.
#Caso o numero já exista la dentro,ele nao será adicionado.No final,serao exibidos todos os valores únicos digitados
#em ordem alfabetica

valor = []
while True:
    n = int(input('Digite um valor: '))
    if not n in valor:
        print('Numero adicionado!')
        valor.append(n)
    else:
        print('Numero nao adicionado')
    continuar = input('Voce quer continuar [Y/N]: ').upper()
    if continuar != 'Y':
        break
    
print(sorted(valor))
        

















#valores = []
#for c in range(0,5):
#    n = int(input('Digite um valor: '))
#    valores.append(n)
#    print('Valor adicionado com sucesso!')
#    for v in range(0,len(valores)):
#        if v == v:
#            print('Valor duplicado! Não vou adicionar...')
#            valores.pop(v)
#print(f'Sua lista ficou {sorted(valores)}')     
        