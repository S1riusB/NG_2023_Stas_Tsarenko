temp = float(input("Please enter your digit: "))
choice = int(input("1.Celsius to fahrenheit  2.Fahrenheit to celsius"))

match choice:
    case 1:
        sum = float(temp * 9/5) + 32
        print(temp," Celsius is:",sum, " Fahrenheit")
    case 2:
        sum = float(temp - 32) * 5/9
        print(temp," Fahrenheit is:",sum, " Celsius")
    
