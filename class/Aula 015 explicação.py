#Aula 015 Explicação
#Laços de repetição(Parte 3)

#Exemplo:
#Tenho um caminho que e muito longo na maça que tem buraco e moeda em cima desse caminho tem um bloco com um trofeu
#entao o que a gente vai fazer: fazer o comando do while e adicionar no laço um pulo e stop = break e isso vai dar
#como missao cumprida.

#O comando em portugues fica:
enquanto verdadeiro:
    se bloco:
        passo
    se buraco:
        pula
    se moeda:
        pega
    se trofeu:
        pula
        interrompa
pega

#O comando em python:
while True:
    if bloco:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break
pega