while True:
    try:
        number = int(input("Enter a non-negative number: "))
        
        if number < 0:
            print("Please enter a non-negative number.")
        else:
            # Calculate the sum from 0 to the user's input
            total = sum(range(number + 1))
            print(f"The sum from 0 to {number} is {total}")
            break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid number.")