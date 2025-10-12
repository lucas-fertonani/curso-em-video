#ex061
#Refaça o desafio 051,lendo o primeiro termo e a razão de uma PA,mostrando os 10 primeiros termos da progressao usando
#estrutura while

result = []
while True:
    n_termo = int(input('Digite o termo: '))
    n_razao = int(input('Digite a razão: '))
    razao_pa = n_termo + n_razao
    result.append(razao_pa)
    print(result)
    






print(n_termo, result,result+n_razao , result+n_razao+n_razao , result+n_razao+n_razao+n_razao , result+n_razao+n_razao+n_razao+n_razao ,result+n_razao+n_razao+n_razao+n_razao+n_razao , result+n_razao+n_razao+n_razao+n_razao+n_razao+n_razao , result+n_razao+n_razao+n_razao+n_razao+n_razao+n_razao+n_razao,result+n_razao+n_razao+n_razao+n_razao+n_razao+n_razao+n_razao+n_razao,end=(' -> '))
            