#Aula 023 prática
#Tratamento de erros e exceções

try:
    n_1 = int(input('Numero 1: '))
    n_2 = int(input('Numero 2: '))
    conta = n_1 - n_2
except:
    print('Error! This is not a int! Try Again')
print(conta)
