#Aula 009
#Manipulando Texto

#frase = 'Curso em video phyton'
#Ele vai criar mini-espaços e cada um desses espaços vao colocar letras
# Curso em video phyton tem 21 caracteres contando com espaços em brancos e o elemento 0
#Algumas operações com esses espaços:






#Tecnica de fatiamento
#Fatiar a string e pegar pedaços delas por exemplo:

#frase = Curso em Video phyton[9] ele vai conseguir somente identificar o nono caracter da cadeia de caracteres
#entao ele vai identificar o 'V'
--------------------------------------------------------------------------------------------------------------------
#Tem outras formar de fazer isso exemplo:
#frase[9:13] ele vai fazer do V que a nona caracter até o e que 12 caracter porque o 13 nao conta
#Ou seja ele vai mostra 'Vide'
--------------------------------------------------------------------------------------------------------------------
#Mais uma forma de mostrar um fatiamento exemplo:
#frase[9:21] ele vai fazer do V que a nona caracter até o 20 caracter por que o 21 nao conta e sempre 1 a menos
#entao vai mostrar: 'Video Phyton'
--------------------------------------------------------------------------------------------------------------------
#Outra forma de mostrar um fatiamento exemplo:
#frase[9:21:2]ou seja eu vou da nona ate a vigesima caracter e o 2 ele vai pulando caracter ele vai pulando de
#duas em duas casas ou seja inves de mostra 'Video phyton' vai mostrar 'Vdo Pto' e as outras letras vao ser ignoradas
#no fatiamento
--------------------------------------------------------------------------------------------------------------------
#Outra forma de fatiamento exemplo:
#frase[:5]ou seja o espaço vazio e onde a palavra vai começar no 0 e o 5 vai ser ate onde a casa vai entao vai ser
#'Curso'
--------------------------------------------------------------------------------------------------------------------
#Outra forma de fatiamento exemplo:
#frase[15:]isso indica pro phyton que quero do caracter 15 ate o final que e o 20 ou seja vai aparecer
#'Python'
--------------------------------------------------------------------------------------------------------------------
#Outra forma de fatiamento exemplo:
#frase[9::3]Ele vai contar da nona caracter ate o final por conta do 0 e o 3 ele vai pulando de 3 em 3 casas
#ou seja vai aparecer 'Ve Ph'







--------------------------------------------------------------------------------------------------------------------

#Tecnica de Analise

#A tecnica de analise a gente vai analisar a string por exemplo:Qual primeira letra da palavra,quantos letras
#minusculas e maiuscula tem etc
#o que a gente vai utilizar é:  len(frase)  len vem de:lenght que é comprimento
#Se eu mando esse comando: len(frase) ele vai mostrar quantos caracteres tem aquela string
---------------------------------------------------------------------------------------------------------------------
#Uma outro forma de analisar a string
# e usar o comando:frase.count('o') esse comando eu estou pedindo que mostre quantos caracteres da letra o
#minuscula tem naquela string por exemplo:'Curso em video phyton' ai nessa string tem 3 caracteres da letra o
#minuscula
---------------------------------------------------------------------------------------------------------------------
#A alteração que o Gustavo guanabara sugere no comando frase.count('o')
#ele sugure trocar por esse comando:frase.count('o',0,13) ou seja ele vai contar do 0 até o 12 caracteres
#quantos 'o' minusculo tem na frase exemplo: frase.count('o',0,13)
# ele vai contar do 'Curso em Video Phyton' ele vai contar que tem somente dos 'o' minusculos 1 letras 'o'
----------------------------------------------------------------------------------------------------------------------
#Outra forma de analise de string
#A gente vai usar esse comando:  frase.find('deo') ou seja ele vai procurar as letras 'deo' e mostrar o momento que
#coemçou as palavras 'deo' que do 'Curso em Video Phyton' sao a 11,12,13 caracteres o 'deo' ele vai me indicar a posição
#das caracteres
----------------------------------------------------------------------------------------------------------------------
#se eu colocar :frase.find('Android') ele vai me mostrar da frase = 'Curso em video phyton' ele vai me mostrar
# -1 ou seja ele me mostrou falando que essa string nao existe dentro dessa variavel
----------------------------------------------------------------------------------------------------------------------
#Outra forma de analise de string
#Se eu colocar o comando: 'Curso' in frase
#Ele vai me mostrar se existe a frase 'Curso' dentro da frase e dentro frase = 'Curso em video Phyton' ele vai
#me mostrar 'Curso' por que existe 'Curso' dentro da string então ele vai escrever 'True' na tela






----------------------------------------------------------------------------------------------------------------------
#Tecnica de transformação
#Uma lista de string ela é imutavel ou seja nao da para mexer nela mas atraves do metodo eu consigo mudar elas
#nao consigo mexer direto nos elementos  mas consigo atraves de metodos

#O primeiro o comando será:
#frase.replace('Phyton','Android')
#Ou seja ele vai replazar o phyton em android ou seja inves de ficar 'Curso em video Phyton' ,Vai ficar
#'Curso em Video Android'      replace significa: 'Trocar,reposicionar'
----------------------------------------------------------------------------------------------------------------------
#Mais uma funcionalidade de transformação
#frase.upper(), upper significa:'pra cima' vai ficar em maiusculas,se eu mandar escrever frase.upper ou seja
#o que ja for maiusculo ele mantem o que nao for maiusculo ele troca pra maiusculo ou seja inves de 'Curso em Video Phyton'
#ele vai colocar 'CURSO EM VIDEO PHYTON'
----------------------------------------------------------------------------------------------------------------------
#Mais uma funcionalidade de transformação:
#frase.lower(),lower significa:'pra baixo'vai ficar em minusculas,se eu mandar escrever frase.lower ou seja
#o que ja for minusculo ele mantem o que nao for minusuculo ele troca pra minusculo ou seja inves de 'Curso em video Phyton'
#ele vai colocar 'curso em video phyton'
----------------------------------------------------------------------------------------------------------------------
#Mais uma funcionalidade de transformação:
#frase.capitalize() ou seja o capitalize vai jogar todas as caracteres para minusculos e so primeiro caracter vai
#ficar em maiusculo ou seja inves de 'Curso em Video Phyton' ele vai mostrar 'Curso em video phyton'
----------------------------------------------------------------------------------------------------------------------
#Mais uma funcionalidade de transformação:
#frase.title() o title ele vai analisar quantas palavras tem a string ele vai fazer uma quebra de frase nos caracteres
#que nao tem letra ,então inves de mostrar 'Curso Em Video Phyton' ele vai transformar pra 'Curso Em Video Phyton'
#a cada nova palavra ele vai mostrar com começo de maiuscula e todos os demais caracteres sao mantidos em minusculos




----------------------------------------------------------------------------------------------------------------------




#Agora vai ser frase = '   Aprenda phyton  '
#coloquei propistalmente 3 espaços em cada lado da string no inicio e no fim 2 e essa string tem total de 18 caracteres
#e colocando comando frase.strip() vai tirar os espaços inuteis no incio e no final então ao inves de
# '   Aprenda phyton  ' vai ser 'Aprenda phyton'
----------------------------------------------------------------------------------------------------------------------
#Agora temos esse comando:
#frase.rstrip() o 'r' que esta no comando significa right=direita e esse comando so vai remover somente o lado direito
#dos espaços entao inves '   Aprenda phyton  ' vai ficar '   Aprenda phyton' e vai ficar somente 17 caracteres
----------------------------------------------------------------------------------------------------------------------
#Agora temos esse comando:
#frase.lstrip() o 'l' que esta no comando significa left=esquerda e esse comando so vai remover somente o lado esquerdo
#dos espaços entao inves '   Aprenda phyton  ' vai ficar 'Aprenda phyton  ' e vai ficar somente 16 caracteres






----------------------------------------------------------------------------------------------------------------------
#Tecnica de divisão
#Posso dividir strings                             frase = 'Curso em Video Phyton'
#Primeira funcionalidade da divisão é:
#frase.split()  ,Em padrão o split e feito no seus espaços,entao simplesmente ele vai pegar onde tem os espaços
#nas strings e fazer uma divisao exemplo:
# 'Curso em Video Phyton' vai ficar 'Curso','em','Video,'Phyton'e cada palavra e colocoda em uma nova lista
#Ou seja 'Curso' e de 0 ate 4 caracteres,'em' e de 0 ate 1 caracter,'Video' e de 0 a 4 caracteres,'Phyton' e de
#0 ate 5 caracteres eles vao ter numerações/lista entao 'Curso' é lista 0, 'em' é lista 1, 'Video' é lista 2 e
#'Phyton' é lista 3
----------------------------------------------------------------------------------------------------------------------
#Tecnica de junção
# agora que eu fiz o split eu tenho listas das palavras das string que eu peguei vou usar esse comando
#pra fazer a junção:
#'-'.join(frase) esse comando vai juntar todos os elementos de frase e vai usar esse separador '-' entao ele
# ia gerar essa string aqui inves de 'Curso' 'em' 'Video' 'Phyton' ele geraria 'Curso-em-video-Phyton e vai ser
#denovo uma cadeia de caracteres de 0 a 20



#O uso de """ tres aspas server para dar print em um texto muito grande