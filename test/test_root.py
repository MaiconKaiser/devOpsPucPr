from src.main import *

def test_root():
    result = root()
    assert result == {}

def test_root_success():
    result = rootSuccess()
    assert result == {"message": "Está funcionando!"}

def test_funcao_teste():
    result = funcaoTeste()
    assert result == {
        "name": "Maicon Kaiser", 
        "idade": "28", 
        "sexo": "Masculino",
        "email": "maicon@teste.com",
        "senha": "teste2"
    }