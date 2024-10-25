text = open("text.txt", "r")
myfile = open("myFile.txt", "w")  #Changed r to w so that it writes instead of reads
line = text.read()  #Added parentheses to call the read method
words = line.split()
for word in words:
    print(word)     #Removed + "\n" as it should be writting to the file not printed
    myfile.write(word + "\n")  #Added a newline character to separate words in the file rather than print

# Close the files
text.close()
myfile.close()