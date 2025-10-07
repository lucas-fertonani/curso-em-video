#ex061
#Refaça o desafio 051,lendo o primeiro termo e a razão de uma PA,mostrando os 10 primeiros termos da progressao usando
#estrutura while

pergunta_termo = int(input('Digite seu termo: '))
pergunta_razao = int(input('Digite sua razão: '))
count = 0
result = 0
while pergunta_termo < pergunta_razao:
    pergunta_termo = int(input('Digite seu termo: '))
    pergunta_razao = int(input('Digite sua razão: '))
    if pergunta_termo > pergunta_razao:
        result = pergunta_termo*pergunta_razao
print(result)
