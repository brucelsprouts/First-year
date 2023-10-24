#activity 7: letterGrade

grade = input("Please enter your grade: ").lower()

if grade == "a":
    print("Excellent! You've got an 'A'")
elif grade == "b":
    print("Good job! You've got a 'B'")
elif grade == "c":
    print("Not bad! You've got a 'C'")
elif grade == "d":
    print("You passed. You've got a 'D'")
elif grade == "f":
    print("Unfortunately, you failed. You've got an 'F'")
else:
    print("Invalid input. Please enter a valid grade (A, B, C, D, or F")