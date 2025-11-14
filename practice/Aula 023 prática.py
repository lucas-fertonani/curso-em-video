#Aula 023 prática
#Tratamento de erros e exceções

try:
    n_1 = int(input('Numero 1: '))
    n_2 = int(input('Numero 2: '))
    conta = n_1 - n_2
except Exception as error:
    print(f'Error! This is not a int! the cause of the error is {error.__class__}')
else:
    print(conta)
finally:
    print('<<<Foi bom sua companinha na calculadora!>>>')


try:
    n_1 = int(input('Numero 1: '))
    n_2 = int(input('Numero 2: '))
    conta = n_1 - n_2
except (ValueError):
    print(f'Erro! esse numero que voce digitou nao tem é um int(número inteiro)')
except (SyntaxError):
    print(f'Isso não é um número!')
else:
    print(conta)
finally:
    print('<<<Foi bom sua companinha na calculadora!>>>')