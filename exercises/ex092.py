#ex092
#Crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre-os(com idade)em um dicionário se por acaso
#a CTPS for diferente de ZERO,o dicionário receberá também o ano de contratação e o salário.Calcule e acrescente,além da
#idade,com quantos anos a pessoa vai se aposentar.
import time
from datetime import datetime
cadastros = []
cadastro = {}
aposentadoria = date.
tempo_atual = time.localtime()
data_atual = tempo_atual.tm_year
tempo_inicial_aposentadoria = datetime(1994,7)
cadastro["Nome"] = str(input('Nome: '))
cadastro["Ano_nascimento"] = int(input('Ano de nascimento: '))
cadastro["Carteira_de_trabalho"] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro["Carteira_de_trabalho"] <= 0:
    print(cadastro)
    print(f'Nome tem o valor {cadastro["Nome"]}')
    print(f'Idade tem o valor {data_atual - cadastro["Ano_nascimento"]}')
    print(f'ctps tem o valor 0')
cadastro['Ano_de_contratação'] = int(input('Ano de contratação: '))
cadastro["Salário"] = float(input('Salário: R$ '))
print(cadastro)
print(f'O nome tem valor {cadastro["Nome"]}')
print(f'idade tem valor {data_atual - cadastro["Ano_nascimento"]}')
print(f'ctps tem valor {cadastro["Carteira_de_trabalho"]}')
print(f'Contratação tem o valor {cadastro["Ano_de_contratação"]}')
print(f'O salário tem o valor {cadastro["Salário"]}')


#codigo do guanabara
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se nao tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-='*30)
for k,v in dados.items():
    print(f' - {k} tem o valor {v}')