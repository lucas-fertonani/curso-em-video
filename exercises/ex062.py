#ex062
#Melhore o desafio 061,perguntando para o usuario se ele quer mostrar mais alguns termos.O programa encerra quando ele
#disser que quer mostrar 0 termos.

result = []
while True:
    n_termo = int(input('Digite o termo: '))
    n_razao = int(input('Digite a razão: '))
    razao_pa = n_termo + n_razao
    result.append(razao_pa)
    print(result)
    if n_termo == 0:
        break