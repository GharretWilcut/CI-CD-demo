
from src.app import add, sub,mult,div,log,sqrt,sin,cos,sqr,percent

def test_add_1():
    assert add(5,6) == 11

def test_add_2():
    assert add(5,6) != 10

def test_add_3():
    assert add(5,6) != 12

def test_subtract():
    assert sub(5, 3) == 2

def test_multiply():
    assert mult(4, 3) == 12

def test_divide_normal():
    assert div(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
