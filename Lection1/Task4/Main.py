import math

def plus(first, second):
    return first + second

def minus(first, second):
    return first - second

def mult(first, second):
    return first * second

def div(first, second):
    return first / second

def stepen(first, second):
    return first ** second

def koren(first):
    return math.sqrt(first)


choice = int(input("1. +\t2. -\t3. *\n4. /\t5. a^b\t 6. √\n"))

first = float(input("First digit: "))
second = float(input("Second digit: "))

match choice:
    case 1:
        print(plus(first, second))
    case 2:
        print(minus(first, second))
    case 3:
        print(mult(first, second))
    case 4:
        print(div(first, second))
    case 5:
        print(stepen(first, second))
    case 6:
        print(koren(first))