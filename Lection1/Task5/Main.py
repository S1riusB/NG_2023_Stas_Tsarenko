import math

a = int(input("First koef "))
b = int(input("Second koef "))
c = int(input("Third koef "))

print(a,"ax^2 + ",b,"x + ",c,"= 0")

D = float
D = b ** 2 + 2 * a * c

x1 = float
x2 = float

x1 = (-b+math.sqrt(D))/(a*2)
x2 = (-b-math.sqrt(D))/(a*2)

print("X1 is: ",x1,"\nX2 is :",x2)