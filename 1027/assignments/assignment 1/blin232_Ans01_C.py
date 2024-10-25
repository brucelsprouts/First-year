"""
CS1026a 2023
Assignment 01 Project 01 - part C
Bruce
251368377
bli232
10/2/2023
"""

#Print out code header
print("Project One <01> - Part C : The Moore the Merrier")

#Function to format the FLOPS with their appropriate unit
def format_flops(flops):
    units = [' ', ' kilo', ' mega', ' giga', ' tera', ' Peta', ' Exa', ' Zetta', ' Yotta']
    for unit in units:
        if flops < 1000: #Concat the appriate unit if theres less than 1000 FLOPS with FLOPS as well as bring the unit to the hundreth decimal place
            return f'{flops:.2f}{unit}FLOPS'
        flops /= 1000

#Prompt user for input values
starting_transistors = int(input("Starting Number of transistors "))
starting_year = int(input("Starting Year: "))
num_years = int(input("Total Number of Years "))

#Initialize variables
transistors = starting_transistors #Value to be adjusted (not necessary but I think its good to keep the consistency, could use starting_transistors.)
year = starting_year    #Value to be adjusted

#Calculate and display Moore's Law for the specified years
print("\nYEAR : TRANSISTORS : FLOPS")
for i in range(num_years // 2 + 2):
    computing_power = transistors * 50
    print(f"{year} {transistors} {format_flops(computing_power)} {computing_power:,}")
    year += 2
    transistors *= 2

#Print out completion of code and personal information
print("\nEND: Project One <01> – Part C")
print("Bruce Lin blin232 251368377")