#Gets age
age = int(input("Enter your age: "))

#Determines wether user can ride
if age >= 9:
    height = float(input("Enter your height in cm: "))
    if height > 130:
        print("You may go on this ride!")
    else:
        print("You are too short for this ride.")
else:
    print("You are too young for this ride.")
