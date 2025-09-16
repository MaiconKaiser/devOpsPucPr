import pytest
from src.main import *

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {}

@pytest.mark.asyncio
async def test_root_success():
    result = await rootSuccess()
    assert result == {"message": "Está funcionando!"}

@pytest.mark.asyncio
async def test_funcao_teste():
    result = await funcaoTeste()
    assert result == {
        "name": "Maicon Kaiser", 
        "idade": "28", 
        "sexo": "Masculino",
        "email": "maicon@teste.com",
        "senha": "teste2"
    }
