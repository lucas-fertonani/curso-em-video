#ex072
#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostra-lo por extenso
extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    n = int(input('Digite um número entre 0 a 20: '))
    if n >= 0 or n < 20:
        break
    print('Tente Novamente')
    novo = int(input('Voce quer continuar [0/1]: '))
    if novo != 'Y':
        break 
print(f'Voce digitou o numero {extenso[n]}')
