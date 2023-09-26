while True:
    age = int(input("Enter your age (or -1 to quit): "))
    
    if age == -1:
        break 
    
    if age >= 18:
        print("You can drive!")
    else:
        print("You cannot drive yet.")