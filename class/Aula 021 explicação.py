#Aula 021
#Funções(Parte 2)

#Coisas importantes das Funções:
#-> Interactive Help            -> Retorno de resultados
#-> docstrings
#-> Argumentos opcionais
#-> Escopo de variáveis


#Interactive Help    -> Ajuda interativa
#Para obter a ajuda interativa do python usamos o comando: help() <- Função interna

#1.Maneira de usar o Interactive Help
#O intercative help e tipo um manual do python quando eu escrevo no terminal do python "help()" ele me retorna qualquer comando pra eu escrever e esse comando que eu
#digitei ele vai falar para que ele serve ou seja um manual do python em sua forma mais resumida,para sair da aba do "help()" nos usamos "quit".

#2.Maneira de usar o Interactive Help
#Posso fazer dentro do programa entao por exemplo: help(if) quando uso isso e executar o meu programa ele vai mostrar o que serve o if e suas funções.

#3.Maneira de usar o Interactive Help
#Posso fazer dentro do programa desse jeito o interactive help: print(for.__doc__) -> ele vai mostrar pra que serve o 'for' e suas funções.



#DOCSTRINGS
#Docstrings é uma string de documentação
#Quando eu crio uma função(def) e quero saber para que ela serve,não vai funcionar o interactive help porque não é um modelo pronto do python,então nesse caso usamos
#as docstrings,as docstrings elas começam uma linha depois do def que eu coloquei.

#Com a docstring posso criar um manual sobre a função que eu criei.
#Como usar uma docstrings:
def escrever(texto):
    """
    -> Ele te pergunta um texto que você quer colocar, e coloca ele entre duas linhas.
    :param texto: parametro sobre o input do texto que ele vai te perguntar.
    :return: sem retorno
    Função criado por Lucas Fertonani
    """
    print('-'*30)
    print(texto)
    print('-'*30)

    t = str(input('Texto: '))
    escrever(t)

help(escrever)



#Parâmetros Opcionais
#Os parametros opcionais sao os parametros que nao preciso colocar o x de determinados parametros da def.
#por exemplo:
def multiplicar(y=2,e=7,g=5):
    z = y*e*g

multiplicar(5,2,7)
multiplicar(3,4)
multiplicar(3)
multiplicar()

#Os parametros opcionais e tipo um if então caso ele nao receber esse determinado parametro ele vai receber o valor que eu coloquei do parametro não recebido ou seja
#de multiplicar(3,4) ele vai receber multplicar (3,4,5) que é = 60.



#Escopo de Variáveis
#O escopo na programação é o local onde uma variável vai existir e o local onde a variável não vai mais existir.

#O escopo local é onde por exemplo uma variavel: texto = 'Fertonani' está colocada no def sobrenome() se eu tentar printar essa variável fora desse 'def sobrenome()'
#vai dar erro dizendo que o 'texto' is not defined, ela só vai funcionar no 'def sobrenome()'.
#Ou seja 'texto' é uma escopo local.

#Quando eu coloco uma variável fora de alguma def ela é considerada uma escopo global.

#e se eu escrevo a mesma variavel do escopo global num local eu crio a variavel global no local e posso colocar algum valor nesse escopo.

#existe um comando que eu posso colocar o escopo global dentro do escopo local olhe:
def numeros(x):
    global y
    r = 6
    f = 7
    t = 32
    print(f'y vale {y}')
    print(f'r vale {r}')
    print(f'f vale {f}')
    print(f't vale {t}')


y = 82
numeros(y)
