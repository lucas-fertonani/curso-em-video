#ex041
#A confederação nacional da natação precisa de um programa que leia um ano de nascimento de um
#atleta e mostre sua categoria de acordo com sua idade:
#-ate 9 anos:MIRIM
#-ate 14 anos:INFATIL
#-ate 19 anos: JUNIOR
#-ate 20 anos:SENIOR
#-Acima:MASTER

ano_nascimento = int(input('Digite seu ano de nascimento: '))
if ano_nascimento >= 2016:
    print('MIRIM')
elif ano_nascimento >= 2011:
    print('INFATIL')
elif ano_nascimento >= 2006:
    print('JUNIOR')
elif ano_nascimento >= 2005:
    print('SENIOR')
elif ano_nascimento < 2005:
    print('MASTER')