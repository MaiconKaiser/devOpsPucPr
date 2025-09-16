from src.main import *;
import pytest

@pytest.fixture
def testRoot():
    result = root();
    yield result;
    assert result == {};

def testRootSuccess():
    result = rootSuccess();
    yield result;
    assert result == {"message": "Está funcionando!"};

def testFuncaoTeste():
    result = funcaoTeste();
    yield result;
    assert result == {
            "name": "Maicon Kaiser", 
            "idade": "28", 
            "sexo": "Masculino",
            "email": "maicon@teste.com",
            "senha": "teste2"
            };