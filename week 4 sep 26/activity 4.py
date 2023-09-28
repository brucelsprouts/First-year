start = int(input("Enter the start of the sequence: "))
end = int(input("Enter the end of the sequence: "))

for number in range(start, end + 1):
    if number % 2 == 0 and number % 3 == 0:
        print(number)