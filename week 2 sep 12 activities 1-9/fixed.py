#Activity 9: Red Squiggly Lines

name = input("What is your name: ")
print("Hello %s, nice to meat you." % name)
age = input("How old are you %s? " % name)
age = int(age)
days = age * 365
days = str(days)
months = age + 12
months = str(months)
print("That is " + days + " days old or " + months + " months!")
print("Your name in all caps is " + name.upper())
print('Your name is %d letters long!' % len(name))
print("Good bye " + name + "!\nI hope you found all the errors.")