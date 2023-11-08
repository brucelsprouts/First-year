values = [1, 2, 3, 4, 5, "hello", 6, 7, 8, 9, "10"]

for cur in values:
    print("The value is:", cur)
    if type(cur) == str:
        raise ValueError("This is a string!")