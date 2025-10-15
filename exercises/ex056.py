
media = []
homem_mais_velho = ''
mulher_menos_de_20 = 0

for idx in range (0,4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    genero = input('Digite seu genero [M/F]: ').upper()
    media.append(idade)
    if idade < 20 and genero == 'F':
        mulher_menos_de_20 =+ 1
    if idade < idade and genero == 'M':
        homem_mais_velho = len(nome)
print(f'A media de idade desse cadastro eh {sum(media)/len(media)} anos')
print(f'O homem mais velho desse cadastro eh {homem_mais_velho}')
print(f'Existem {mulher_menos_de_20} mulheres com menos de 20 anos')


































































































#ex056


maior_idade = 0
print('----- 1 PESSOA -----')
nome_1 = str(input('Nome: '))
idade_1 = int(input('Idade: '))
sexo_1 = str(input('Sexo [M/F]: '))
print('----- 2 PESSOA -----')
nome_2 = str(input('Nome: '))
idade_2 = int(input('Idade: '))
sexo_2 = str(input('Sexo [M/F]: '))
print('----- 3 PESSOA -----')
nome_3 = str(input('Nome: '))
idade_3 = int(input('Idade: '))
sexo_3 = str(input('Sexo [M/F]: '))
print('----- 4 PESSOA -----')
nome_4 = str(input('Nome: '))
idade_4 = int(input('Idade: '))
sexo_4 = str(input('Sexo [M/F]: '))

media_idade = (idade_1 + idade_2 + idade_3 + idade_4) / 4
print(' ')
print(f'A media de idade desse grupo e de {media_idade}')
print(' ')

#O homem mais velho

if sexo_1 == 'M' and idade_1 > idade_2 and idade_3 and idade_4:
    print(f'o homem {nome_1} de {idade_1} anos e o mais velho')
if sexo_2 == 'M' and idade_2 > idade_1 and idade_3 and idade_4:
    print(f'o homem {nome_2} de {idade_2} anos e o mais velho')
if sexo_3 == 'M' and idade_3 > idade_1 and idade_2 and idade_4:
    print(f'o homem {nome_3} de {idade_3} anos e o mais velho')
if sexo_4 == 'M' and idade_4 > idade_1 and idade_2 and idade_3:
    print(f'o homem {nome_4} de {idade_4} anos e o mais velho')


#Quantidade de mulheres com menos de 20 anos
if sexo_1 == 'F' and idade_1 < 20:
    print('Existe 1 mulher com menos de 20 anos')
elif sexo_2 == 'F' and idade_2 < 20:
    print('Existe 1 mulher com menos de 20 anos')
elif sexo_3 == 'F' and idade_3 < 20:
    print('Existe 1 mulher com menos de 20 anos')
elif sexo_4 == 'F' and idade_4 < 20:
    print('Existe 1 mulher com menos de 20 anos')
elif sexo_1 and sexo_2 == 'F' and idade_1 and idade_2 < 20:
    print('Existem 2 mulheres com menos de 20 anos')
elif sexo_3 and sexo_4 == 'F' and idade_3 and idade_4 < 20:
    print('Existem 2 mulheres com menos de 20 anos')
elif sexo_1 and sexo_3 == 'F' and idade_1 and idade_3 < 20:
    print('Existem 2 mulheres com menos de 20 anos')
elif sexo_4 and sexo_2 == 'F' and idade_4 and idade_2 < 20:
    print('Existem 2 mulheres com menos de 20 anos')
elif sexo_1 and sexo_2 and sexo_3 == 'F' and idade_1 and idade_2 and idade_3 < 20:
    print('Existem 3 mulheres com menos de 20 anos')
elif sexo_1 and sexo_2 and sexo_3 and sexo_4 == 'F' and idade_1 and idade_2 and idade_3 and idade_4 < 20:
    print('Existem 4 mulheres com menos de 20 anos')