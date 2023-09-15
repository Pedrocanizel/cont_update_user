import psycopg2
import pandas as pd

def get_connect():
    con = psycopg2.connect(host='', database='',
    user='', password='')
    return con



def atualizar(data):
    query = 'UPDATE schema.tabela SET ' 
    conn = get_connect()
    cursor = conn.cursor()
    for key,value in data.items():
        query = query + f"{key}='{value}', "
    query = query[:len(query)-2]
    query = query + f""" where search_id  = '{data['name']}-{data['email']}'"""
    cursor.execute(query)
    conn.commit()
    conn.close()

def conferir_search_id(name, email):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""SELECT COUNT(search_id) FROM schema.tabela WHERE search_id = '{name}-{email}'"""
    contagem = pd.read_sql_query(query, con=conn)
    contagem = contagem['count'].loc[0]
    return contagem
