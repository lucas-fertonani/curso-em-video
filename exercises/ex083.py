#ex083
#Crie um programa onde o usuário digita uma expressão qualquer que use parenteses.Seu aplicativo deverá analisar
#se a expressão passada está com os parenteses abertos ou fechados na ordem correta

expr = str(input('Digite uma expressao: '))
expressao = []
for x in expr:
    if x == '(':
        expressao.append('(')
    elif x == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break
if len(expressao) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta errada')















#expressao = []

#ex = str(input('Digite uma expressao: '))
#expressao.append(ex)
#if not expressao in (''):
#    print('Use uma expressao valida')
#else:
#    print('Expressao valida')
