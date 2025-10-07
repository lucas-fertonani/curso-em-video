#ex032
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano_bissexto = int(input('Qual ano você quer saber se é bissexto: '))
if ano_bissexto % 4 == 0:
    if ano_bissexto % 100 != 0:
        print('Bissexto')
    elif ano_bissexto % 400 == 0:
        print('Bissexto')
    else:
        print(f'O ano de {ano_bissexto} não é bissexto')
else:
    print(f'O ano de {ano_bissexto} não é bissexto')