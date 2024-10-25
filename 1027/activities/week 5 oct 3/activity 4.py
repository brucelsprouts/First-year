def printNumbersBetween(num1,num2):
    for x in range(num1,num2+1):
        print(x)

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    printNumbersBetween(num1,num2)

main()