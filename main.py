from fastapi import FastAPI

app = FastAPI();


@app.get("/")
async def root():
    return {};

@app.get("/dados")
async def funcaoTeste():
    return {
            "name": "Teste", 
            "idade": "28", 
            "sexo": "Masculino",
            "email": "teste@teste.com",
            "senha": "teste"
            };