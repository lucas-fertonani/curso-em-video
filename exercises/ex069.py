#ex069
#Crie um programa que leia a idade e sexo de várias pessoas.A cada pessoa cadastrada,o programa deverá perguntar
#se usuário quer ou nao continuar.No final mostre:
#A) Quantas pessoas tem mais de 18 anos
#B) Quantos homens foram cadastrados
#C) Quantas mulheres tem menos de 20 anos
maior_de_18 = 0
homens = 0
mulheres_menos_20 = 0
while True:
    idade = int(input('Qual é sua idade: '))
    sexo = input('Digite seu sexo [M/F]: ').upper()
    print('Dados salvos com sucesso!')
    continuar = input('Você quer continuar? [Y/N]').upper()
    if idade > 18:
        maior_de_18 += 1
    if sexo == 'M':
        homens =+ 1
    if idade < 20 and sexo == 'F':
        mulheres_menos_20 += 1
    if continuar != 'Y':
        break
print(f'Nesse cadastro existem {maior_de_18} pessoas maiores de 18 anos')
print(f'Nesse cadastro existem {homens} homens')
print(f'Nesse cadastro existem {mulheres_menos_20} mulheres menores de 20 anos')
    



    