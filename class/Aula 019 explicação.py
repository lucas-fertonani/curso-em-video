#Aula 019
#Variáveis compostas (Dicionários)

#Os dicionários são estruturas semelhantes as listas e tuplas só que dessa vez eu consigo ter indices literais.
#Eu consigo personalizar os indíces.
#Para declarar um dicionário são identificados pelo: dados = {} ou dados = dict{}
#por exemplo na lista está:
#list = [60,1.62]
#dados = {'Peso': 60 , 'Altura': 1.62}
#agora vai ter indice peso e indice altura inves de indice 0 e 1

#dados = {'Peso': 60, 'Altura': 1.62}
#print(dados['Peso']) -> 60
#print(dados['Altura']) -> 1.62

#Como adicionar elementos em um dicionário
#dados = {'Peso': 60, 'Altura': 1.62}
#dados['name'] = 'Felipe'
#del dados['Altura'] -> vai eliminar a altura e vai ficar so o peso e o name

#Vamos criar um exemplo pra sabermos entre diferenças de valores,chaves e itens
#book = {'Title' = 'Arthur Morgan',
#        'Synopese' = 'Redemption'
#         'Numbers of sales' = 400000 
#}
#print(book.values()) -> ele vai me retornar todos os valores do dicionário da parte de cima dele.
#print(book.keys()) -> ele vai pegar todos os valores do dicionario deles debaixo:Title,Synopose e Numbers of sales
#print(book.items()) -> se eu quero ambos valores keys e values.

#Exemplo de items com o for:
#for k,v in book.items():
#   print(f'O {k} é {v}') -> Codigo de saída -> O title é Arthur morgan
#                                               O Synopose é Redemption
#                                               O Number of sales é 400000

#Criar uma lista onde tem cada dicionario dentro
# dicionario = {'Country' = 'United States'
#               'Population = 523.432.012
#               'The most famous city' = 'New york'}
# 
# paises = []
# paises.append(dicionario)
# print(paises) -> Codigo de saida = ['Country' = 'United States'
#               'Population = 523.432.012
#               'The most famous city' = 'New york']