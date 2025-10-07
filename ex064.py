#ex064
#Crie um programa que leia varios numeros inteiros pelo teclado.O programa so vai para quando o usuario digitar o valor
#999, que a condição de parada.No final mostre quantos numeros foram digitados e qual foi a soma entre eles(descosiderando
# o flag)
result = []
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    else:
        result.append(n)
print(len(result),sum(result))
print(sum(result)/len(result))
        























#pergunta_num = ''
#soma = 0
#desconsiderar = -999
#while pergunta_num not in [999]:
#    pergunta_num = int(input('Digite um valor: '))
#    if pergunta_num > soma: 
#        soma = 999- pergunta_num + soma 
#print(soma)