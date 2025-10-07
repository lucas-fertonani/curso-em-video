#ex049
#Refaca o desafio 009,mostrando a tabuada que o usuario escolher,so que agora usando o laco for

tabuada = int(input('Digite o numero que quer sua tabuada: '))
tabuada_1_resposta = 1*tabuada
tabuada_2_resposta = 2*tabuada
tabuada_3_resposta = 3*tabuada
tabuada_4_resposta = 4*tabuada
tabuada_5_resposta = 5*tabuada
tabuada_6_resposta = 6*tabuada
tabuada_7_resposta = 7*tabuada
tabuada_8_resposta = 8*tabuada
tabuada_9_resposta = 9*tabuada
tabuada_10_resposta = 10*tabuada

tabuada_resposta_final = (tabuada_1_resposta,tabuada_2_resposta,tabuada_3_resposta,tabuada_4_resposta,tabuada_5_resposta,tabuada_6_resposta,tabuada_7_resposta,tabuada_8_resposta,tabuada_9_resposta,tabuada_10_resposta)
for x in tabuada_resposta_final:
    print(x)
