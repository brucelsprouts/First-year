try:
    filename = input("Enter filename: ")
    infile = open(filename, "r")
    line = infile.readline()
    value = int(line)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except ValueError:
    print("Error: The content in the file is not a valid integer.")
finally:
    if 'infile' in locals():
        infile.close()
