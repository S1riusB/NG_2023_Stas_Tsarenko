a = float(input("Please enter your digit: "))
x = int(input("1.Celsius to fahrenheit  2.Fahrenheit to celsius"))
sum = float


if (x == 1):

 sum = float(a * 9/5) + 32
 print(a," Celsius is:",sum, " Fahrenheit")
elif (x == 2):
 sum = float(a - 32) * 5/9
 print(a," Fahrenheit is:",sum, " Celsius")
else:
 print("Error!")