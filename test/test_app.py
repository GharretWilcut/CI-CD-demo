
from src.app import add,sub,mult,div,log,sqrt,sin,cos,square,percent
import math
import pytest

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
        
def test_square():
    assert square(5) == 25

def test_sqrt():
    assert sqrt(25) == 5

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-9)

def test_log():
    assert round(log(10), 5) == round(math.log(10), 5)

def test_log_zero_or_negative():
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-5)

def test_sin():
    assert round(sin(math.pi/2), 5) == 1.0

def test_cos():
    assert round(cos(0), 5) == 1.0

def test_percentage():
    assert percent(200, 10) == 20
