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

# Function to calculate FLOPS (Floating-Point Operations Per Second)
def calculate_flops(transistors):
    return transistors * 50  # Assuming each transistor results in 50 FLOPS

# Function to format FLOPS in terms of unit definition
def format_flops(flops):
    units = ['FLOPS', 'KiloFLOPS', 'MegaFLOPS', 'GigaFLOPS', 'TeraFLOPS', 'PetaFLOPS', 'ExaFLOPS', 'ZettaFLOPS', 'YottaFLOPS']
    for unit in units:
        if flops < 1000:
            return f"{flops:.2f} {unit}"
        flops /= 1000

# Get user input for starting transistors, starting year, and number of years to calculate
starting_transistors = int(input("Enter the starting number of transistors: "))
starting_year = int(input("Enter the year to start the calculations from: "))
num_years = int(input("Enter the number of years to calculate: "))

# Initialize variables
current_transistors = starting_transistors
current_year = starting_year

# Print header
print(f"{'Year':<6}{'Transistors':<20}{'FLOPS (Unit Definition)':<35}{'FLOPS (Actual)':<15}")

# Calculate and display Moore's Law estimates
for _ in range(num_years // 2):
    flops = calculate_flops(current_transistors)
    flops_formatted = format_flops(flops)
    print(f"{current_year:<6}{current_transistors:<20}{flops_formatted:<35}{flops:.2f}")
    
    # Double the number of transistors for the next two-year cycle
    current_transistors *= 2
    current_year += 2

#Print out completion of code and personal information
print("END: Project One <01> – Part A")
print("Bruce Lin blin232 251368377")