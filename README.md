# Instalar os pacotes
- fastapi
- requests
- json
- pymongo
- dotenv

# Para rodar
- uvicorn main:app --port 8000
- uvicorn main:app --port 8001
- uvicorn main:app --port 8002

# Testando

Acesse a URL: http://localhost:8000/api/docs

# Objetivo

### Rota de soma de dados
A rota busca valores numericos de outros nós para poder realizar a soma com o valor passado por parâmetro pelo usuário.

### Rota do mongoDB
Acesso ao banco para leitura e inserção de dados através de qualquer nó da aplicação.
