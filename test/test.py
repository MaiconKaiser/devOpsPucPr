from src.main import *;

def testRoot():
    result = root();
    assert result == {};

def testRootSuccess():
    result = rootSuccess();
    assert result == {"message": "Está funcionando!"};

def testFuncaoTeste():
    result = funcaoTeste();
    assert result == {
            "name": "Maicon Kaiser", 
            "idade": "28", 
            "sexo": "Masculino",
            "email": "maicon@teste.com",
            "senha": "teste2"
            };