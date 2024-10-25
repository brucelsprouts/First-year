infile = open("input.txt","r")
for line in infile:
    line = line.rstrip("El,p\na")
    print(line, end="")
infile.close()