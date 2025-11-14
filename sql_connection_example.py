# SQL conneciton usage (example)

import psycopg2

def get_conn():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

def save_record_on_memory(name: str, age: int, gender: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, age, gender) VALUES (%s, %s, %s)",
        (name, age, gender)
    )
    conn.commit()
    cursor.close()
    conn.close()





#DESAFIO CONCLUIDO
def airport():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name_airport FROM airport"
    )
    get = cursor.fetchall()
    cursor.close()
    conn.close()
    return get
print(airport())

# SQL conneciton usage (example)

import psycopg2

def get_conn():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

# def save_record_on_memory(name: str, age: int, gender: str):
#     conn = get_conn()
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO users (name, age, gender) VALUES (%s, %s, %s)",
#         (name, age, gender)
#     )
#     conn.commit()
#     cursor.close()
#     conn.close()

# def get_records():
#     conn = get_conn()
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT * FROM users"
#     )
#     records = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return records