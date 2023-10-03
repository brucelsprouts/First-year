def printNumbers():
    for num in range(1, 11):
        print(num, end=' ')

def printReverse():
    for num in range(10, 0, -1):
        print(num, end=' ')

# Calling the functions to display the numbers
print("Numbers from 1 to 10:")
printNumbers()

print("\nNumbers in reverse order from 10 to 1:")
printReverse()
