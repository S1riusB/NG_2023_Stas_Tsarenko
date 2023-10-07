import math

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def stepen(a, b):
    return a ** b

def koren(a):
    return math.sqrt(a)


x = int(input("1. +\t2. -\t3. *\n4. /\t5. a^b\t 6. √\n"))

a = float(input("First digit: "))
b = float(input("Second digit: "))

match x:
    case 1:
        print(plus(a, b))
    case 2:
        print(minus(a, b))
    case 3:
        print(mult(a, b))
    case 4:
        print(div(a, b))
    case 5:
        print(stepen(a, b))
    case 6:
        print(koren(a))