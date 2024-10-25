# Define an empty dictionary to store sets
dictionary = {
    'even': set(),
    'odd': set(),
    'three': set()
}

# Loop through numbers from 0 to 20
for num in range(0, 21):
    if num % 2 == 0:  # Check if the number is even
        dictionary["even"].add(num)  # Add even number to the "even" set
    if num % 2 != 0:  # Check if the number is odd
        dictionary["odd"].add(num)  # Add odd number to the "odd" set
    if num % 3 == 0:  # Check if the number is a multiple of 3
        dictionary["three"].add(num)  # Add multiple of 3 to the "three" set

# Print the dictionary
for key, value in dictionary.items():
    print(f"{key}: {value}")