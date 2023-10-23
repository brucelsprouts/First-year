#Activity 4: gradeAscend
grade1 = int(input("Enter the first grade: "))
grade2 = int(input("Enter the second grade: "))

if grade1 > grade2:
    print("Grades in ascending order: " + str(grade2) + ", " + str(grade1))
else:
    print("Grades in ascending order: " + str(grade1) + ", " + str(grade2))
