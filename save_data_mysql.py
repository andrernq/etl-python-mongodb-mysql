import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def connect_mysql():
    mysql_host = os.getenv("MYSQL_HOST")
    mysql_user = os.getenv("MYSQL_USER")
    mysql_password = os.getenv("MYSQL_PASSWORD")
    cnx = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password
    )
    print(cnx)
    return cnx

def create_cursor(cnx):
    cursor = cnx.cursor(buffered=True)
    return cursor

def create_database(cursor, db_name):
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')
    print(f'Base de dados {db_name} criada.')

def show_databases(cursor):
    cursor.execute('SHOW DATABASES;')
    print('\nBase de dados existentes:')
    for db in cursor:
        print(db)

def create_product_table(cursor, db_name, tb_name):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {db_name}.{tb_name}(
                id VARCHAR(100),
                Produto VARCHAR(100),
                Categoria_Produto VARCHAR(100), 
                Preco FLOAT(10,2),
                Frete FLOAT(10,2),
                Data_Compra DATE,
                Vendedor VARCHAR(100),
                Local_Compra VARCHAR(100),
                Avaliacao_Compra INT,
                Tipo_Pagamente VARCHAR(100),
                Quantidade_Parcelas INT,
                Latitude FLOAT(10,2),
                Longitude FLOAT (10,2),
                PRIMARY KEY (id));
        """)
    print(f'\nTabela {tb_name} criada no banco de dados {db_name}.')

def show_tables(cursor, db_name):
    cursor.execute(f'USE {db_name};')
    cursor.execute('SHOW TABLES;')
    print(f'\nTabela(s) do banco de dados {db_name}:')
    for tb in cursor:
        print(tb)

def read_csv(path):
    df = pd.read_csv(path)
    return df

def add_product_data(cnx, cursor, df, db_name, tb_name):
    lista_dados = [tuple(row) for i, row in df.iterrows()]
    sql = f'INSERT INTO {db_name}.{tb_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
    cursor.executemany(sql, lista_dados)
    print(f'\nForam inseridos {cursor.rowcount} dados na tabela {tb_name}.')
    cnx.commit()