N = int(input("Enter a number (N >= 1): "))

if N < 1:
    print("Please enter a number greater than or equal to 1.")
else:
    for i in range(1, N + 1):
        line = ' '.join(map(str, range(1, i + 1)))
        print(line)
