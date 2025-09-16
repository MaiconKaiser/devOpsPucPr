from fastapi import FastAPI

app = FastAPI();


@app.get("/")
async def root():
    return {};

@app.get("/status")
async def rootSuccess():
    return {"message": "Está funcionando!"};

@app.get("/dados")
async def funcaoTeste():
    return {
            "name": "Maicon Kaiser", 
            "idade": "28", 
            "sexo": "Masculino",
            "email": "maicon@teste.com",
            "senha": "teste2"
            };

@app.get("/saudacao")
async def saudacao(nome: str = "visitante"):
    return {"mensagem": f"Olá, {nome}!"}


@app.get("/soma")
async def soma(a: int, b: int):
    return {"resultado": a + b}