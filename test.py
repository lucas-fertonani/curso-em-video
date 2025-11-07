pessoas = []

for c in range(0,2):
    pessoa = {}
    pessoa["name"] = str(input('Nome: '))
    pessoa["age"] = int(input('Idade: '))
    pessoa["year_birth"] = int(input('Year of birth: '))
    pessoa["month_birth"] = int(input('Month of birth: '))
    while pessoa['month_birth'] > 12 or pessoa['month_birth'] < 1:
        print('A data tem que ser entre 1 e 12')
        pessoa["month_birth"] = int(input('Month of birth: '))

    pessoas.append(pessoa)

print(pessoas)
