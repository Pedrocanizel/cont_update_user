import psycopg2
import datetime
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='localhost', database='bit_pro',
    user='postgres', password='123')
    return con



def atualizar(data):
    query = 'UPDATE public.cadastro_usuario SET ' 
    conn = get_connect()
    cursor = conn.cursor()
    for key,value in data.items():
        query = query + f"{key}='{value}', "
    query = query[:len(query)-2]
    query = query + f" where email = '" + data['email'] + "'"
    cursor.execute(query)
    conn.commit()
    conn.close()





    
  # UPDATE public.cadastro_usuario SET column1 = value1, column2 = value2, WHERE email LIKE '%{email}%';
  # 
  # "email": "pedrocanizela666@gmail.com",
  #     "name": "Pedro Canizela",
  #     "password": "cabide123",
  #     "razao_social": "corinthians",
  #     "sobrenome": "Canizela",
  #     "idade": "pedro",
  #     "cpf": "04880703923",
  #     "cnpj": "123456789",
  #     "telefone": "899418875",
  #     "estado": "pr",
  #     "cadastro_criado_em": "2023-03-06 09:28:42.454398"
    