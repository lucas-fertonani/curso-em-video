#ex029
#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h,mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7.00 reais por cada km acima do limite

km = float(input('quantos km/h estava seu carro: '))

if km > 80:
    calculadora = (km - 80) * 7
    print(f'Você sera multado você deverá pagar {calculadora} R$')

