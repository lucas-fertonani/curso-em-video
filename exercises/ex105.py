#ex105
#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#-Quantidade de notas
#-A maior nota
#-A menor nota
#-A média da turma
#-A situação(opcional)

#Adicione também as docstrings da função.

def categoriza_media(media):
    if media < 5:
        return "RUIM"
    if media < 9:
        return 'RAZOAVEL'
    
    return 'BOA'


def calcula_notas(notas: list):
    """
notas(*n, sit=False)
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sits: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    n_maior = 0
    n_menor = 999
    count = 0
    total = 0
    media = 0
    
    for nota in notas:
        if nota > n_maior:
            n_maior = nota
        if n_menor > nota:
            n_menor = nota
        count =+ 1
        total = total + nota
        media = total / count

    
    resultados = {
    'total': total,
    'maior': n_maior,
    'menor': n_menor,
    'média': media,
    'situação': categoriza_media(media)
    }
    return resultados

print(calcula_notas([4.0,3.2,7.6,9.5]))
help(calcula_notas)


    