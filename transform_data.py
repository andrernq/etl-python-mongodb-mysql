from extract_and_save_data import connect_mongo, create_connect_db, create_connect_collection
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def visualize_collection(col):
    for doc in col.find():
        print(doc)

def rename_column(col, col_name, new_name):
    col.update_many({}, {'$rename': {f'{col_name}': f'{new_name}'}})

def select_category(col, category):
    query = {'Categoria do Produto': category}
    lista_categoria = []
    for doc in col.find(query):
        lista_categoria.append(doc)
    return lista_categoria

def make_regex(col, regex):
    query = {'Data da Compra': {'$regex': f'{regex}'}}
    lista_produtos = []
    for doc in col.find(query):
        lista_produtos.append(doc)
    return lista_produtos

def create_dataframe(lista):
    df = pd.DataFrame(lista)
    return df

def format_date(df):
    df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')
    df['Data da Compra'] = df['Data da Compra'].dt.strftime('%Y-%m-%d')

def save_csv(df, path):
    df.to_csv(path, index=False)
    print(f'O arquivo {path} foi salvo com sucesso.')