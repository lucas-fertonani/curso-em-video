#Faca um programa que leia um numero inteiro e diga se ele é um numero primo
tot = 0
num = int(input('Digite um valor: '))
for x in range(1,num + 1):
    if num % x == 0:
     tot += 1
    print(f'o numero {num} foi divisivel por {tot} vezes')
else:
   print(f'O numero {num} foi divisivel por {tot} vezes')


if tot == 2:
      print(f'por isso o numero {num} eh primo')
else:
    print(f'O numero {num} nao eh primo')
     

    
    
    




