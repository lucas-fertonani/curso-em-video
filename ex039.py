#ex039
#Faça um programa que leia o ano de nascimento de um jovem e informa,de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar
#-Se e hora de ele se alistar
#-Se ja passou na hora de se alistar
#seu programa tambem devera mostrar o tempo que falta ou que passou do prazo
idade = int(input('Que idade voce tem jovem: '))
prazo_nao_passado = 18-idade
prazo_passado = idade-18
if idade <= 17:
    print(f'Voce ainda vai se alistar ao serviço militar! falta {prazo_nao_passado} anos!')
elif idade == 18:
    print('Voce está na hora de se alistar!')
elif idade >= 19:
    print(f'Voce ja passou da hora de se alistar,passou {prazo_passado} anos!')
