import math
def add(a,b):
    return a + b

def mult(a,b):
    return a * b
    
def sub(a,b):
    return a - b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def square(a):
    return a * a

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(a)

def log(a):
    if a <= 0:
        raise ValueError("log undefined for a <=0")
    return math.log(a)

def sin(a): return math.sin(a)
def cos(a): return math.cos(a)

def percent(a,p): 
    return a * (p/100)




