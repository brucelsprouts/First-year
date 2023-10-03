"""
CS1026a 2023
Assignment 01 Project 01 - part A
Bruce
251368377
bli232
10/2/2023
"""

#Print out code header
print("Project One <01> - Part A : Fibonacci Sequence")

#Get user input for the value up to which the sequence should be generated
end_number = int(input("Sequence ends at: "))

#Print of first 2 hard coded lines
print("0: 0 0")
print("1: 1 1")

#Initialize the first two terms of the sequence
a, b = 0, 1

#Determine and print the rest of the sequence
for i in range(2, end_number + 1):
    # Calculate the next term
    next_term = a + b
    a, b = b, next_term

    # Print the next term in the sequence
    print(f"{i}: {next_term} {next_term:,}")

#Print out completion of code and personal information
print("\nEND: Project One <01> – Part A")
print("Bruce Lin blin232 251368377")