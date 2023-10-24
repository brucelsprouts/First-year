"""
CS1026a 2023
Assignment 01 Project 01 - part B
Bruce
251368377
bli232
10/2/2023
"""

#Print out code header
print("Project One <01> - Part B : Prime Choice")

#Function to check if a number is prime
def is_prime(number): 
    if number <= 1:     #Non prime negative, 0, and 1
        return False
    if number == 2:     #Exclude 2 from even numbers as prime
        return True
    if number % 2 == 0: #Even numbers considered not prime
        return False

    #Check for factors up to the square root of the number
    for i in range(3, number, 2): #Incriment by 2 to check divisibility for all odd numbers
        if number % i == 0:
            return False
    return True

#Get user input for the range and ensure its valid
from_range = int(input("\nPrime Numbers starting with: "))    #Starting number in range
to_range = int(input("and ending with: "))                  #Ending number in range

if to_range < from_range:   #Validates whether range is valid and swaps if isnt
    print(f"Incorrect Input: {from_range} is greater than {to_range}")
    print("The numbers have been automatically switched.")
    temp = from_range       #Temp variable avaible so that the variables can be swapped
    from_range = to_range
    to_range = temp

#Find and display prime numbers within the specified range
print("\nPrime numbers within the specified range:")
for number in range(from_range, to_range + 1):
    if is_prime(number) == True:    #Print prime number if true
        print(f"{number} is prime")

#Print out completion of code and personal information
print("\nEND: Project One <01> – Part B")
print("Bruce Lin blin232 251368377")