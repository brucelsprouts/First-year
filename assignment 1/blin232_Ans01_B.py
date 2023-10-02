"""
CS1026a 2023
Assignment 01 Project 01 - part B
Bruce
251368377
bli232
10/2/2023
"""

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    # Check for factors up to the square root of the number
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Get user input for the range and ensure it's valid
while True:
    try:
        from_range = int(input("Prime Numbers starting with: "))
        to_range = int(input("and ending with: "))
        
        if from_range < 0 or to_range < 0:
            print("Invalid input. Please enter non-negative integers.")
        elif to_range < from_range:
            print("Invalid input. TO range must be greater than or equal to FROM range.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Find and display prime numbers within the specified range
print("\nPrime numbers within the specified range:")
for number in range(from_range, to_range + 1):
    if is_prime(number):
        print(f"{number}: Prime")

#Print out completion of code
print("END: Project One <01> – Part A")

#Print out name and western username
print("Bruce Lin blin232")