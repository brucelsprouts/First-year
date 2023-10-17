values = [1, 2, 3, 4, 5]
newValues = values.copy()  # Fix 1: Create a copy of the 'values' list

# Fix 2: Change the loop range to len(values) instead of len(values)+1
for i in range(len(values)):    
    values[i] += 1
    print("Old Value at index {} is: {} ".format(i, newValues[i]))  # Fix 3: Correct the format statement
    print("New Value at index {} is: {} \n".format(i, values[i]))  # Fix 4: Correct the format statement