#ex067
#Faça um programa que mostre a tabuada de vários números,um de cada vez,para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
tabuada = 0
while True:
    t = int(input('Quer ver a tabuada de qual valor: '))
    if t < 0:
        break
    else:
        print(f'1 x {t} = {t}')
        print(f'2 x {t} = {t*2}')
        print(f'3 x {t} = {t*3}')
        print(f'4 x {t} = {t*4}')
        print(f'5 x {t} = {t*5}')
        print(f'6 x {t} = {t*6}')
        print(f'7 x {t} = {t*7}')
        print(f'8 x {t} = {t*8}')
        print(f'9 x {t} = {t*9}')
        print(f'10 x {t} = {t*10}')