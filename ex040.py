#ex040
#Crie um programa que leia duas notas de um aluno e calcule sua media,mostrando uma mensagem no final,
#de acordo com a media atingida:
#-Media abaixo de 5.0:reprovado
#-Media entre 5.0 e 6.9:recuperação
#-Media de 7.0 ou superior:Aprovado
primeira_nota_aluno = float(input('Digite sua primeira nota: '))
segunda_nota_aluno = float(input('Digite sua segunda nota: '))
soma_das_notas = (primeira_nota_aluno + segunda_nota_aluno)/2
print(f'A media desse aluno e {soma_das_notas}')
if soma_das_notas < 5.0:
    print('REPROVADO!')
elif soma_das_notas < 7.0:
    print('RECUPERAÇÃO')
elif soma_das_notas >= 7.0:
    print('APROVADO!')

