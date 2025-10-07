#ex046
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,indo
#de até 10 a 0, com uma pausa de 1 segundo entre eles


import time
print('Contagem regressiva para os fogos de artificio')
for x in range (10,-1,-1):
    time.sleep(1.0)
    print(x)
print('BOOM!')