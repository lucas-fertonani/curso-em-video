#ex113
#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaint(text=''):
    value = input(text)
    
    return value.isnumeric()

    

def leiafloat(text=''):
    value = input(text) # sempre é string

    # Verificando se o usuário digitou algo
    if not value:
        return False
    
    # Valor é númerico?
    if not value.replace('.','').isnumeric():
        return False
    
    # Tem ponto?
    if not ('.' in value):
        return False
    
    return True


    


while True:
    print(leiaint('Numero inteiro: '))

