#aula 011 explicação

#Cores no terminal

# Padrão: ANSI
#Esse ANSI ele tem o chamado de "escape sequence"
#O codigo ANSI ela começa com a contra barra "\" e depois vem o codigo
# Um dos codigos de cores que mais funciona com o python e o codigo 033

#Sempre que voce quiser representar uma cor em python voce usa esse comando:
#    \033[m
#Entre a chave e o ,m, vai preencher com coisas e essas coisas podem ser: nenhum codigo,um codigo,dois codigos
#ou três codigos

#Exemplo com três codigos:
#\033[style.,text.,back m
#style=estilo do texto
#text= texto
#back/background = curtifundio
# entao o comando vai ficar o estilo que voce quer o tipo de texto que voce quer o background que voce quer
#exemplo:
#\033[0;33;44m
#Os codigos pra estilo sao:
#0 = none
#1 = Bold = negrito
#4 = Underline = sublinhar
#7 = Invertes as configurações o que eu coloquei pra fundo ele vai colocar pra letra e que eu coloquei de letra
#vai ficar de fundo

#Codigos de textos são:
#30 = O texto vai ficar branco
#31 = O texto vai ficar vermelho
#32 = O texto vai ficar verde
#33 = O texto vai ficar amarelo
#34 = O texto vai ficar azul
#35 = O texto vai ficar roxo
#36 = O texto vai ficar ciano
#37 = O texto vai ficar cinza

#codigos de background são:
#40 = O background vai ficar branco
#41 = O background vai ficar vermelho
#42 = O background vai ficar verde
#43 = O background vai ficar amarelo
#44 = O background vai ficar azul
#45 = O background vai ficar roxo
#46 = O background vai ficar ciano
#47 = O background vai ficar cinza


#Se eu quero que fique preto pra background uso esse comando:
#\033[m

#Se eu quero que fique preto pra letra uso esse comando:
#\033[7;30m