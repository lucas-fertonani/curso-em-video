#ex091
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
# SQL conneciton usage (example)

import psycopg2
from time import sleep
import random


def get_conn():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

def save_record_on_memory(jogador_name: str, dado: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO jogo_de_dados (jogador_name, dado) VALUES (%s, %s)",
        (jogador_name, dado)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_top3():
    conn = get_conn()
    query = '''
        SELECT * FROM jogo_de_dados
        ORDER BY dado DESC
        LIMIT 3;
    '''
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records



dado = [x for x in range(1, 10000)]

qtd_jogadores = int(input('Quantidade de jogadores: '))

for idx in range(1,qtd_jogadores+1):
    dado_aleatorio = random.choice(dado)
    nome = f'jogador{idx}'
    save_record_on_memory(nome,dado_aleatorio)


records = get_top3()

for record in records:
    print(record[1], record[2])


