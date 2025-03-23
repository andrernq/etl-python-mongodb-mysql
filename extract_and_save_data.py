from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def connect_mongo():
    # criando um novo cliente e conectando ao servidor
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri, server_api=ServerApi('1'))

    # enviando um ping para conferir se a conexão foi realizada
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

def create_connect_db(client, db_name):
    db = client[db_name]
    return db

def create_connect_collection(db, col_name):
    collection = db[col_name]
    return collection

def extract_api_data(url):
    response = requests.get(url)
    return response.json()

def insert_data(col, data):
    docs = col.insert_many(data)
    n_docs_inseridos = len(docs.inserted_ids)
    return n_docs_inseridos
