from src.main import *;
import pytest

@pytest.fixture
def test_root():
    result = root();
    yield result;
    assert result == {};

@pytest.fixture
def test_root_success():
    result = rootSuccess();
    yield result;
    assert result == {"message": "Está funcionando!"};

@pytest.fixture
def test_funcao_teste():
    result = funcaoTeste();
    yield result;
    assert result == {
            "name": "Maicon Kaiser", 
            "idade": "28", 
            "sexo": "Masculino",
            "email": "maicon@teste.com",
            "senha": "teste2"
            };