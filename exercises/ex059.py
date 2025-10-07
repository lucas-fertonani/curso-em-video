#ex059
#Crie um programa que leia dois valores e mostre no menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa


pergunta_num_1 = ''
pergunta_num_2 = ''
escolha = ''
while True:
    pergunta_num_1 = int(input('Digite um numero: '))
    pergunta_num_2 = int(input('Digite o segundo numero: '))
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair do programa')
    escolha = int(input('Digite qual desses voce quer: '))
    if escolha == 1:
        print(pergunta_num_1 + pergunta_num_2)
    if escolha == 2:
        print(pergunta_num_1 * pergunta_num_2)
    if escolha == 3:
        if pergunta_num_1 > pergunta_num_2:
            print(f'{pergunta_num_1} e maior do que {pergunta_num_2}')
        if pergunta_num_2 > pergunta_num_1:
            print(f'{pergunta_num_2} e maior do que {pergunta_num_1}')
        if pergunta_num_1 == pergunta_num_2:
            print(f'Os numero sao iguais')
    if escolha == 5:
        print('fim')
        break






























# num_1 = int(input('Digite um valor: '))
# num_2 = int(input('Digite o segundo valor: '))
# print('[1] somar')
# print('[2] multiplicar')
# print('[3] maior')
# print('[4] novos numeros')
# print('[5] sair do programa')
# escolha = int(input('Digite qual voce quer: '))
# if escolha == 1:
#     print(num_1 + num_2)
# if escolha == 2:
#     print(num_1 * num_2)
# if escolha == 3:
#     if num_1 > num_2:
#         print(f'{num_1} e maior do que {num_2}')
#     if num_2 > num_1:
#         print(f'{num_2} e maior do que {num_1}')
# if escolha == 4:
#     num_3 = int(input('Digite um valor: '))
#     num_4 = int(input('Digite o segundo valor: '))
#     print('[1] somar')
#     print('[2] multiplicar')
#     print('[3] maior')
#     print('[4] novos numeros')
#     print('[5] sair do programa')
#     escolha_1 = int(input('Digite qual voce quer: '))
#     if escolha_1 == 1:
#         print(num_3 + num_4)    
#     if escolha_1 == 2:
#         print(num_3 * num_4)
#     if escolha_1 == 3:
#      if num_4 > num_3:
#         print(f'{num_4} e maior do que {num_3}')
#     if num_3 > num_4:
#         print(f'{num_3} e maior do que {num_4}')
# if escolha_1 == 5 or escolha == 5:
#     print('Fim')
