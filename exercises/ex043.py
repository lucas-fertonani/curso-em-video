#ex042
#Desenvolva uma logica que leia o peso de uma altura de uma pessoa,calcule seu IMC e mostre seu status
#,de acordo com a tabela abaixo
#Abaixo de 18.5= abaixo do peso
#Entre 18.5 e 25= peso ideal
#25 ate 30=sobrepeso
#30 ate 40=obesidade
#acima de 40:obesidade morbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso**2/altura
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')