#ex051
#Desenvolva um programa que leia o primeiro termo e a razao de uma PA.No final mostre os 10 primeiros termos dessa
#progressao

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite sua razao: '))
soma_razao_e_termo = primeiro_termo+razao
for c in range(primeiro_termo,primeiro_termo+20,razao):
    print(c,end=(' -> '))
