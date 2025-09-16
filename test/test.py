from src.main import *;

def testRoot():
    assert root() == {};

def testRootSuccess():
    assert rootSuccess() == {"message": "Está funcionando!"};

def testFuncaoTeste():
    assert funcaoTeste() == {
            "name": "Maicon Kaiser", 
            "idade": "28", 
            "sexo": "Masculino",
            "email": "maicon@teste.com",
            "senha": "teste2"
            };