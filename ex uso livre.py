


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

idade = ''
while True:
    idade = int(input('Digite sua idade: '))
    if idade != int:
        print('Desculpe so aceitamos numeros')
    if idade > 120 or idade < 0:
        print('Insira um valor razóavel')
    else:
        break

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


total_pedido = []
pizza = 50.90
refri = 10.80
while True:
    print('Pizza 50,90R$')
    print('Refri 10,80R$')   
    print('Qual vai ser sua opção?')
    print('Pizza [1]')
    print('Refri [2]')
    print('Finalizar [3]')
    escolha = int(input('Digite qual voce quer: '))
    if escolha == 1:
        print('Pizza adicionado ao seu pedido!')
    if escolha == 2:
        print('Refri adicionado ao seu pedido ')
    if escolha != 1 or 2 or 3:
        print('Opcao invalida')
    if escolha == 3:
        print(f'Seu pedido total deu ')
        break