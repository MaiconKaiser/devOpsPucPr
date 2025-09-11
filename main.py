from fastapi import FastAPI

app = FastAPI();


@app.get("/")
async def root():
    return {};

@app.get("/status")
async def root():
    return {"message": "Está funcionando!"};

@app.get("/dados")
async def funcaoTeste():
    return {
            "name": "Maicon Kaiser", 
            "idade": "28", 
            "sexo": "Masculino",
            "email": "maicon@teste.com",
            "senha": "teste"
            };