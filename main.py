from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import json
from pymongo import MongoClient
import dotenv

username = dotenv.get_key(".env", "MONGO_USERNAME")
password = dotenv.get_key(".env", "MONGO_PASSWORD")

client = MongoClient(f"mongodb+srv://{username}:{password}@senai.0iyluzc.mongodb.net/?retryWrites=true&w=majority")
db = client["fastapi_db"]
collection = db["fastapi_collection"]

#Criação da API com rotas de teste e de soma de valores 
app = FastAPI(
    title="Projeto Teste",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

#Rota de teste
@app.get("/")
async def root():
    """Rota de teste"""
    return {"message": "Hello World"}

#Rota de teste com retorno de HTML
@app.get("/html")
def get_html():
    """Retorna um HTML"""
    html_content = """
        <html>
            <body>
                <h1> Teste </h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)

#Soma de valores coletados de outras APIs
@app.get("/soma_valores/{valor}")
def soma_valores(valor: int):
    """Soma valores de outras APIs"""
    valor1 = requests.get('http://localhost:8001/pegar_valor')
    valor2 = requests.get('http://localhost:8002/pegar_valor')

    return {"soma": valor1.json() + valor2.json() + valor}

#Disponibiliza um valor para ser somado
@app.get("/pegar_valor")
def pegar_valores():
    """Retorna um valor para ser somado"""
    return 10


#Conexão com o MongoDB
@app.get("/data")
async def le_dados():
    """Lê dados do banco de dados"""
    try:
        data = collection.find_one()
        return {"data": data["data"] if data else None}
    except:
        return {"data": "Erro ao ler dados!"}

@app.post("/data")
async def escreve_dados(data: str):
    """Insere dados no banco de dados"""
    try:
        collection.delete_many({})
        collection.insert_one({"data": data})
        return {"message": "Dados inseridos com sucesso!"}
    except:
        return {"message": "Erro ao inserir dados!"}

