import pytest
from calculadora import suma

def test_1():
    assert suma(2, 3) == 5

def test_2():
    assert suma(2.5, 3.5) == 6.0

def test_3():
    assert suma(2, 3.5) == 5.5

def test_letras():
    assert suma(2, "texto") == "Error"

def test_letras1():
    assert suma("texto", 3) == "Error"

def test_letras2():
    assert suma("texto", "texto") == "Error"
