import math

first = int(input("First koef "))
second = int(input("Second koef "))
third = int(input("Third koef "))

print(first,"ax^2 + ",second,"x + ",third,"= 0")

D = second ** 2 + 2 * first * third

x1 = (-second+math.sqrt(D))/(first*2)
x2 = (-second-math.sqrt(D))/(first*2)

print("X1 is: ",x1,"\nX2 is :",x2)