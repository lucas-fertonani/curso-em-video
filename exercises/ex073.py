#ex073
#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,na ordem
#de colocação.Depois mostre:
#A)Apenas os 5 primeiros colocados
#B)Os últimos 4 colocados da tabela
#C)Uma lista com os times em ordem alfabética
#D)Em que posição na tabela está o time Chapecoense

Campeonato_Brasileiro = ('Palmeiras','Flamengo','Cruzeiro','Mirassol','Botafogo','Bahia','Fluminense','São Paulo','Bragantino','Ceará','Vasco','Corinthians','Grêmio','Atlético-MG','Internacional','Santos','Vitória','Fortaleza','Juventude','Sport')
print(f'lista do brasileirão: {Campeonato_Brasileiro}')
print(' ')
print(f'Os primeiros 5 são {Campeonato_Brasileiro[0:5]}')
print(' ')
print(f'Os 4 últimos são {Campeonato_Brasileiro[16:]}')
print(' ')
print(f'Times em ordem alfabetica {sorted(Campeonato_Brasileiro)}')