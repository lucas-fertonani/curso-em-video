#Aula 010 -Condições(Parte 1)

#Condições simples e compostas

#eu tenho um carro eu quero chegar na linha de chegada mas eu tenho que
#ir pra frente depois esquerda,frente,direita,frente,direita,frente,frente,esquerda,frente e parar depois
#quais comandos eu uso:

#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.direita()
#carro.siga()
#carro.direita()
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.pare()

#essas linhas de codigo eu vou chamar de "Estrutura Sequencial" que significa que é feito numa sequência

#agora se eu tivesse como eu ir pra dois caminhos:
#o que eu iria usar é chamado Biforcação
#Biforcação:Ter duas possibilidades ou mais no meu caso e esquerda e direita

#esquerda-->
#Carro.siga()
#Carro.direita()
#Carro.siga()
#Carro.direita()
#Carro.esquerda()
#Carro.siga()
#Carro.direita()
#Carro.siga()
#Carro.pare()

#Agora se fosse pra esquerda:
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.pare()

#Ou seja mudou muito as rotas que dava pra fazer por conta da Biforcação
#O carro.siga e o carro.pare vao acontecer sempre por conta que os unicos que podem tomar uma iniciativa de se mover

#Vamos pegar um exemplo:
#O fluxo verde vai ser o da direita que é o programa
#O fluxo vermelho vai ser o da esquerda que e o programa tambem
# com todas essas rotas eles sempre vao chegar no comando:
#carro.pare() ou seja os dois comando sao diferentes mas tem a mesma conclusão

#Agora vamos usar esse comando:
# if carro.esquerda() esse comando faz:
# se virar pra esquerda faz essa rota aqui o carro:
#Carro.siga()
#Carro.direita()
#Carro.siga()
#Carro.direita()
#Carro.esquerda()
#Carro.siga()
#Carro.direita()
#Carro.siga()
#Carro.pare()

#Agora se eu usar esse comando:
# if carro.direita() esse comando faz:
# se virar pra direita faz essa rota aqui o carro:                        if-->Significa:Se

#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.pare()

#Agora esse comando faz:
# if carro.esquerda()
# else carro.direita()                                 else-->Significa:senão
#Estou fazendo que se ele nao fizer a rota da esquerda,ele obviamente vai fazer a rota da direita
#entao com esse comando ele faz isso:

#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.pare()

#E na programação e nao posso fazer assim ae que vai entrar uma coisa chamada "Representação Estruturada"ou
#a "Representação Indentada"
#entao em geral o que esta escrito vai ficar assim:

#if carro.esquerda():
 #Carro.siga()
 #Carro.direita()
 #Carro.siga()
 #Carro.direita()
 #Carro.esquerda()
 #Carro.siga()
 #Carro.direita()
 #Carro.siga()
 #Carro.pare()
#else:
 #carro.siga()
 #carro.esquerda()
 #carro.siga()
 #carro.esquerda()
 #carro.siga()
#carro.pare()

#--->Como voce pode ver as rotas tem um espaço a mais e o else e if nao tem isso a gente chama de
# "Indentação"

#Agora vai reorganizar o codigo

# if carro.esquerda():
#   bloco True
#else:
#   bloco False

#O caminho na programção a gente vai chamar de "bloco"
#False=Falso,True=Verdadeiro



#Entao condição é:
# if carro.esquerda():
#   bloco True
#else:
#   bloco False

#Nunca sera executado os dois ao mesmo tempo
