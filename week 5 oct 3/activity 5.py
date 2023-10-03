def sumOfEvenNumbers(start,end):
    return_value = 0
    if start > end:
        return(0)
    else:
        for x in range(start,end+1):
            if x%2 == 0:
                return_value = return_value + x
    return(return_value)

def main():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    sum_number = sumOfEvenNumbers(first_number,second_number)
    print(f"The sum of even numbers between {first_number} and {second_number} (exclusive) is: {sum_number}")

main()