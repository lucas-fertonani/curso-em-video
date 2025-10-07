#renda=(input('qual é sua renda atual?'))
#print('Sua renda atual eh de{}!'.format(renda))

#nome=input('qual eh seu nome?')
#print('Prazer em te conhecer{}!'.format(nome))

#n1=int(input('Digite um valor:'))
#n2=int(input('Digite outro valor:'))
#print('Sua soma eh de {}!'.format(n1+n2))

#n1=(input('digite um valor'))
#print(type(n1))

#n1 = int(input('Digite uma base: '))
#n2 = int(input('Digite um exponente: '))
#print ('Sua potencia da o resultado de {}!'.format(n1**n2))

#n1 = int(input('Digite um dividendo: '))
#n2= int(input('Digite um divisor: '))
#print('O resto da sua divisão eh {}!'.format(n1/n2))

#n1 = int(input('Digite um dividendo: '))
#print('Sua divisão inteira é de {}!'.format(n1//n2))

#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro valor: '))
#s=n1 + n2
#m=n1 * n2
#d=n1 / n2
#di=n1 // n2
#e=n1 ** n2
#print('A soma eh {} a multplicação eh {} e a divisão eh {:.3f}'.format(s,m,d))
#print('A divisão inteira eh {} e a potência eh {}'.format(di,e))

#frase = 'Curso em video phyton'
#print('Tem quatro {} letras o nessa frase'.format(frase.count('o')))

##print(frase.split())


#print("""A amizade consegue ser tão complexa.
#Deixa uns desanimados, outros bem felizes.
#É a alimentação dos fracos
#É o reino dos fortes.

#Faz-nos cometer erros
#Os fracos deixam se ir abaixo
#Os fortes erguem sempre a cabeça
#Os assim assumem-nos.

#Sem pensar conquistamos
#o mundo geral
#e construímos o nosso pequeno lugar,
#deixando brilhar cada estrelinha.

#Estrelinhas.
#Doces, sensíveis, frias, ternurentas.
#Mas sempre presentes em qualquer parte.
#Os donos da amizade.""")
#import random
#jogada_do_usuario = input('Qual será sua jogada PEDRA,PAPEL OU TESOURA:')
#lista = ['PEDRA','PAPEL','TESOURA']
#jogada_do_computador = random.choices(lista)
#if  jogada_do_usuario == jogada_do_computador:
    #print('Empate')

#if jogada_do_usuario == 'TESOURA' and jogada_do_computador == 'PEDRA':
    # print('Você perdeu')

#if jogada_do_usuario == 'TESOURA' and jogada_do_computador == 'PAPEL':
   # print('Você ganhou!')

#if jogada_do_usuario == 'PEDRA' and jogada_do_computador == 'PAPEL':
  #  print('Você perdeu!')

#if jogada_do_usuario == 'PEDRA' and jogada_do_computador == 'TESOURA':
 #   print('Você ganhou')

#if jogada_do_usuario == 'PAPEL' and jogada_do_computador == 'TESOURA':
#    print('Você perdeu!')

#if jogada_do_usuario == 'PAPEL' and jogada_do_computador == 'PEDRA':
 #   print('Você ganhou!')

nome_de_usuario = 'Lucas'
senha = 'Abcd1234'
pergunta_usuario = input('Qual é seu nome de usuario: ')
pergunta_senha = str(input('Digite sua senha: '))
if not nome_de_usuario == pergunta_usuario:
    print('Usuario errado!')
else:
    print(' ')
if not senha == pergunta_senha:
    print('Senha Incorreta tente novamente!')
if senha == pergunta_senha:
    print('Acesso-liberado,bem-vindo Lucas!')

