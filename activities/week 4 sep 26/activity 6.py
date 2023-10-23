while True:
    try:
        N = int(input("Enter an integer (N >= 1): "))
        if N < 1:
            print("Good Bye!")
            break 

        for num in range(1, N + 1):
            if num % 2 != 0:
                print(num) 

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
