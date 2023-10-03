#Prompt the user to enter the number of values they want to use
n = int(input("How many numbers do you want to use today?"))

if n > 0:
    #Prompt the user to enter the first number
    firstValue = int(input("Enter the first number: "))

    #Initialize variables for tracking largest, smallest, and total
    largest = firstValue
    smallest = firstValue
    total = firstValue

    counter = 0
    #Loop to input and process the remaining numbers
    while counter < (n - 1):
        current = int(input("Enter the next number: "))
        total = total + current
        counter = counter + 1

        #Check if the current number is smaller than the smallest
        if current < smallest:
            smallest = current
        #Check if the current number is larger than the largest
        elif current > largest:
            largest = current

    #Calculate and print the average of the values
    print("The average of the values is: ", total / n)
    #Print the smallest and largest values
    print("The smallest of the values is {}".format(smallest))
    print("The largest of the values is {}".format(largest))
    #Calculate and print the range of the values
    print("The range of the values is {}".format(largest - smallest))
else:
    #If the user entered a non-positive number, inform them that no values will be used
    print("You did not want to use any numbers today.")