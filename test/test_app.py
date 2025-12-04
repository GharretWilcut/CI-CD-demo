
from src.app import add 

def test_add_1():
    assert add(5,6) == 11

def test_add_2():
    assert add(5,6) != 10

def test_add_3():
    assert add(5,6) != 12