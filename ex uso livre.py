


#senha_correta = 'Nhandeara80'
#pergunta = ''
#while senha_correta != pergunta:
#    pergunta = input('Digite sua senha: ')
#print('Sucesso')



#result = []
#somar_nota = 0
#hile True:
#    pergunta_nota = float(input('Digite sua nota: '))
#    if pergunta_nota <= -1:
#       break
#    else:
#        result.append(pergunta_nota)
#print('A media de todas essas notas sao:',sum(result)/len(result))


#saldo_atual = 500
#deposito = 700
#hile True:
#   print('Bom dia senhor! qual desses opções você quer?')
#    print('Ver Saldo [1]')
#    print('Fazer depósito [2]')
#   print('Sair [3]')
#    escolha = int(input('Faça sua escolha: '))
#    if escolha == 1:
#       print('Seu saldo e de 500 reais')
#    if escolha == 2:
#        deposito = float(input('Digite quando voce quer depositar: '))
#    if deposito > saldo_atual:
#       print('Deposito Negado!')
 #       print('Deposito feito com sucesso!')
 #   if escolha == 3:
 #       break

#ex007 sobre o while:Crie um jogo simples onde o programa "pensa" em um número e o usuário tenta adivinhar.
#import random
#list = [0,1,2,3,4,5,6,7,8,9,10]
#jogada_do_computador = random.choice(list)
#jogada_do_usuario = ''
#contador = 0
#while jogada_do_usuario != jogada_do_computador:
#    jogada_do_usuario = int(input('Digite um número: '))
#    contador += 1
#print(f'Parabéns você adivinhou o número {jogada_do_computador} em {contador} tentativas!')



#inversor = ''
#ergunta = ''
#contador = 0 
#while not pergunta:
#    pergunta = str(input('Qual palavra voce quer inverter: '))
#    inversor = pergunta[::-1]
#print(inversor)

#numero_final = 50
#numero_incial = 1
#somar = 0 
#hile numero_incial < numero_final:
#    print('Vou colocar os numeros de 0 a 50 impares')
lista = []
for c in range(0,3):
    pergunta = int(input('Valor: '))
    lista.append(pergunta)
print(lista)