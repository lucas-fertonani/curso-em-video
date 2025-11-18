#ex115
#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.



cadastro = []
cadastro_dict = {}

FILE_NAME = 'contatos.txt'


def menu_principal():
    print()
    print('-'*30)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar Nova Pessoa')
    print('3 - Sair do Sistema')
    print('-'*30)



def save_txt_line(line):
    with open(FILE_NAME, 'a') as file:
        file.write(f'{line}\n')

def read_all_text():
    with open(FILE_NAME, 'r') as file:
        content = file.read()
        lines = content.split('\n')
        for line in lines:
            print(line)

def opcao_2():
    nome = input('nome ')
    idade = input('idade ')
    linha_para_ser_salva = f'{nome} & {idade}'
    save_txt_line(linha_para_ser_salva)    

def opcao_1():
    read_all_text()




def sistema_modularizado():
    while True:
        menu_principal()
        try:
            opcao = int(input('Opção: '))
            if not (opcao in [1,2,3]):
                raise ValueError('Voce tem que escolher a opcao 1, 2 ou 3') 
        except ValueError as e:
            print(e)
        
        if opcao == 1:
            opcao_1()
        if opcao == 2:
            opcao_2()
        if opcao == 3:
            break
        
sistema_modularizado()

