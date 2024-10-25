#list
unique_numbers = []

#asks for the 10 numbers
while len(unique_numbers) < 10:
    user_input = input("Enter a unique number: ")
    number = int(user_input)

    #checks uniqueness
    if number not in unique_numbers:
        unique_numbers.append(number)
    else:
        print("Number is not unique. Please enter a unique number.")

print("Unique numbers list:", unique_numbers)