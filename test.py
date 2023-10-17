def myFunction(strings):  
    count=0  
    for s in strings:  
        if len(s) > 2:  
            count+=1  
    return count  
  
# Create a list of words  
words=["hello","good","nice","as","at","baseball","absorb"]  
  
# Call the function and print the output  
print(myFunction(words))