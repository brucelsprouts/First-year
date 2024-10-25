print("Enter two numbers to divide:")

while True:
    try:
        dividend = float(input("Dividend: "))
        divisor = float(input("Divisor: "))
        quotient = dividend / divisor
        break
    except ZeroDivisionError:
        print("Can not divide by zero!\n")
    except ValueError:
        print("Invalid input!\n")
        
print("The result is %.2f" % quotient)