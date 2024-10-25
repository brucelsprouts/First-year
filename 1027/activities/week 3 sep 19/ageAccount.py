#Activity 6: ageAccount
age = int(input("Please enter your age: "))

has_account = input("Do you have an account? (Yes/No): ").strip().lower()

if age >= 18 and has_account == "yes":
    print("You have full access to all features.")
elif age >= 18 and has_account == "no":
    print("You can create an account to access all features.")
elif age < 18 and has_account == "yes":
    print("You have limited access to certain features.")
else:
    print("You need to be 18 or older and create an account to access all features.")
