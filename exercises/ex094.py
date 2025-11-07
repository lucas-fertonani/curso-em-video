#Crie um programa que leia nome,sexo e idade de várias pessoas,guardando os dados de cada pessoa em um dicionário e todos os dicionarios em uma lista.No final,
#mostre:
#A-)Quantas pessoas foram cadastradas 
#B-)A média da idade do grupo
#C-)Uma lista com todas as mulheres.
#D-)Uma lista com todas as pessoas acima da média


##CODIGO QUE O GUANABARA FEZ
































#CODIGO QUE EU FIZ
# count_woman = 0
# cadastro_lista = []
# lista_idade = []
# while True:
#     cadastro_dicionario = {}
#     cadastro_dicionario["nome"] = str(input('Nome: '))
#     cadastro_dicionario["idade"] = int(input('Idade: '))
#     cadastro_dicionario["sexo"] = str(input('Sexo: [M/F]: ')).upper()
#     cadastro_lista.append(cadastro_dicionario)
#     lista_idade.append(cadastro_dicionario["idade"])
#     continuar = str(input('Você quer continuar? [S/N]: '))
#     if continuar in 'Nn':
#         break
# media_idade = sum(lista_idade)/len(lista_idade)
# print('-='*30)
# if len(cadastro_lista) == 1:
#     print(f'- So existe {len(cadastro_lista)} pessoa')
# else:
#     print(f'- O grupo tem {len(cadastro_lista)} pessoas')


#     print(f'- A media de idade desse grupo eh {media_idade} anos')

# if cadastro_dicionario["sexo"] == 'F':
#     count_woman =+ 1
# print(f'- Existe {count_woman} mulheres nesse grupo')

#for p in lista_idade:
    if p["idade"] > media_idade:
        for k,v in p.items():
            print(f'{k} = {v}',end=(''))
        print()
print('<<<ENCERRADO>>>')