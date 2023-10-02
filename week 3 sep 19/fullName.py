#Activity 3: fullName
full_name = input("Please enter your FULL NAME: ")

name_parts = full_name.split()

if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[1]

    print("First letter: " + first_name[0] + ", Last letter: " + last_name[0])
else:
    print("Your input does not contain at least two parts (first name and last name).")