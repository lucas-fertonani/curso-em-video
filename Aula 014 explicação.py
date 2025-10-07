#Aula 014 explicação

#Laços de repetição(parte 2)

#por exemplo
#tenho um caminho pra chegar ate a maçã mas nao sei quantos passos eu tenho que dar pra chegar na maça
#entao utilizaremos outra estrutura de repetição
#Chamaremos ela de "enquanto"= while
#entao ficaria assim:
#enquanto ele nao chegar na maça continue dando os passos
#Usaremos o "while" quando nao sabemos o final
# e depois ele vai sair da estrutura de repetição e vai fazer o comando de pegar a maça
#Chamaremos essa estrutura de :Estrutura de repetição com teste logico

#Na nossa lingua fica assim:
enquanto não :maça:
    passo
pega

#Na linguagem python ficaria assim:
while not maça:
    passo
pega

#Segundo exemplo
#teremos um caminho pra chegar ate a maça
![](2025-10-02-18-19-42.png)
#teremos um caminho pra chegar ate a maça onde que existe bloco vazio e moeda e nao sei o limite 
#entao ficaria assim pra chegar na maça
while not maça:
    if True
    passo
    if buraco
    pule
    if True
    pega
pega
# e com isso ele vai voltar la pra cima e fazer a mesma estrutura de repetição
# e quando chega na maça todo esse comando que ta em cima se torna falso por que chegou na maça
# e com isso ele sai da estrutura de repetição e pega a maça

#Como representar em portugues esse comando:
enquanto nao maça:
    se chao:
        passo
        se pulo:
            pula
            se moeda:
                pega
pega

#Como representar em python esse comando:
while not maça:
    if chao:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega