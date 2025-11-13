#Aula 021 prática
#Funções(parte 2)





# return com o bool
print('Calculadora pra ver se um numero é divisivel por 2')
print('True = eh possivel dividir por 2')
print('False = não eh possivel dividir por 2')

def divisao(number=0):
    if number % 2 == 0:
        return True
    else:
        return False

num = int(input('Number: '))
print(divisao(num))