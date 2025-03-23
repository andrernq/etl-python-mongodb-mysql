# Projeto de integração Python, MongoDB e MySQL

Este projeto realiza a extração, transformação e transferência de dados (ETL) utilizando Python, MongoDB e MySQL.

## 📌 Tecnologias utilizadas
- Python
- MongoDB
- MySQL
- Pandas
- Requests
- Dotenv

## ⚙️ Instalação e configuração

Para rodar o projeto corretamente, siga os passos abaixo:

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/andrernq/etl-python-mongodb-mysql.git
cd etl-python-mongodb-mysql
```

### 2️⃣ Crie um ambiente virtual e ative-o
Recomendamos o uso de um ambiente virtual para organizar as dependências do projeto.

- **No Linux/macOS**:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

- **No Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3️⃣ Instale as dependências
Após ativar o ambiente virtual, instale as bibliotecas necessárias executando:
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o arquivo `.env`
O projeto utiliza um arquivo `.env` para armazenar as credenciais do banco de dados.  
Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais:

```
MONGO_URI=sua_uri_mongodb
MYSQL_HOST=seu_host_mysql
MYSQL_USER=seu_usuario_mysql
MYSQL_PASSWORD=sua_senha_mysql
```

## 🚀 Como executar o projeto

### 1️⃣ Executar a extração e salvar no MongoDB:
```bash
python extract_and_save_data.py
```

### 2️⃣ Transformar os dados:
```bash
python transform_data.py
```

### 3️⃣ Salvar os dados no MySQL:
```bash
python save_data_mysql.py
```

## 📂 Estrutura do projeto
```
├── extract_and_save_data.py
├── transform_data.py
├── save_data_mysql.py
├── extract_and_save_data_project.ipynb
├── transform_data_project.ipynb
├── save_data_mysql_project.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

## ✍️ Autor
- [André Ronqui](https://github.com/andrernq)
