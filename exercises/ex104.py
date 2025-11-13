#ex104
#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas
#valor númerico.

#Ex: n = leiaint('Digite um n').

def leiaint(text=''):
    value = input(text)
    if value.isnumeric():
        return int(value)
    return
    


while True:
    verificar = leiaint('Digite um número: ')
    if verificar:
        print('Isso é um número')
    else:
        print('invalid number')
        break
