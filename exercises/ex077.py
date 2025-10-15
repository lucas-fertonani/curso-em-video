#ex077
#Crie um programa que tenha uma tupla com várias palavras(não usar acentos).Depois disso,você deve mostrar,para
#cada palavra,quais sao suas vogais
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
vogais = ('a','e','i','o','u')
for p in palavras:
    print(f'Na palavra {p.upper()} temos:')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra)
