#ex035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triangulo


primeiro_cm_triangulo = float(input('Digite o comprimento da primeira linha reta: '))
segundo_cm_triangulo = float(input('Digite um comprimento da segunda linha reta: '))
terceira_cm_triangulo = float(input('Digite um comprimento da terceira linha reta: '))

if primeiro_cm_triangulo + segundo_cm_triangulo > terceira_cm_triangulo:
    print('Da para formar um triangulo')
else:
    print('Não da para formar um triangulo')